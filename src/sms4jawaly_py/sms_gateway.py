import json
from typing import List, Optional, Dict, Any
import requests
from .models import SMSRequest, SMSResponse, BalanceResponse

class SMSGatewayError(Exception):
    """Exception raised when an API request fails."""
    pass

class SMSGateway:
    """Main class for interacting with the 4jawaly SMS Gateway API."""
    
    BASE_URL = 'https://api-sms.4jawaly.com/api/v1'
    
    def __init__(self, api_key: str, api_secret: str, sender: str):
        """Initialize the SMS Gateway client.
        
        Args:
            api_key: Your API key
            api_secret: Your API secret
            sender: Default sender name
        """
        self.api_key = api_key
        self.sender = sender
        self._session = requests.Session()
        self._session.headers.update({
            'Authorization': api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        })
    
    def send_sms(
        self,
        numbers: List[str],
        message: str,
        sender: Optional[str] = None
    ) -> SMSResponse:
        """Send SMS to one or multiple recipients.
        
        Args:
            numbers: List of phone numbers
            message: Message content
            sender: Optional sender name (if different from default)
        
        Returns:
            SMSResponse object containing status and job IDs
        
        Raises:
            SMSGatewayError: If the API request fails
        """
        request = SMSRequest(
            numbers=numbers,
            message=message,
            sender=sender or self.sender
        )
        
        response = self._session.post(
            f'{self.BASE_URL}/send',
            json=request.dict()
        )
        
        if not response.ok:
            raise SMSGatewayError(
                f'API request failed with status: {response.status_code}'
            )
        
        try:
            return SMSResponse.parse_obj(response.json())
        except Exception as e:
            raise SMSGatewayError(f'Failed to parse response: {e}')
    
    def send_single_sms(self, number: str, message: str) -> SMSResponse:
        """Send SMS to a single recipient.
        
        Args:
            number: Phone number
            message: Message content
        
        Returns:
            SMSResponse object containing status and job ID
        
        Raises:
            SMSGatewayError: If the API request fails
        """
        return self.send_sms([number], message)
    
    def get_balance(
        self,
        is_active: Optional[int] = None,
        order_by: Optional[str] = None,
        order_by_type: Optional[str] = None
    ) -> BalanceResponse:
        """Get account balance and package information.
        
        Args:
            is_active: Filter by active packages (0 or 1)
            order_by: Sort field
            order_by_type: Sort direction (asc or desc)
        
        Returns:
            BalanceResponse object containing account information
        
        Raises:
            SMSGatewayError: If the API request fails
        """
        params: Dict[str, Any] = {}
        
        if is_active is not None:
            params['is_active'] = is_active
        if order_by:
            params['order_by'] = order_by
        if order_by_type:
            params['order_by_type'] = order_by_type
        
        response = self._session.get(
            f'{self.BASE_URL}/balance',
            params=params
        )
        
        if not response.ok:
            raise SMSGatewayError(
                f'API request failed with status: {response.status_code}'
            )
        
        try:
            return BalanceResponse.parse_obj(response.json())
        except Exception as e:
            raise SMSGatewayError(f'Failed to parse response: {e}')
    
    def close(self):
        """Close the HTTP session."""
        self._session.close()
    
    def __enter__(self):
        """Support for context manager protocol."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support for context manager protocol."""
        self.close()
