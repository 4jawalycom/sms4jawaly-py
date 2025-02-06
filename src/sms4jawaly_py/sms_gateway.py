import json
from typing import List, Optional, Dict, Any
import requests
from .models import SMSRequest, SMSResponse, BalanceResponse, SenderNamesResponse

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
        self.api_secret = api_secret
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
        data = {
            'numbers': numbers,
            'message': message,
            'sender': sender or self.sender
        }
        
        print(f"Sending request to {self.BASE_URL}/send")
        print(f"Headers: {self._session.headers}")
        print(f"Data: {json.dumps(data, indent=2)}")
        
        response = self._session.post(
            f'{self.BASE_URL}/send',
            json=data
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
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
        params = {}
        if is_active is not None:
            params['is_active'] = is_active
        if order_by:
            params['order_by'] = order_by
        if order_by_type:
            params['order_by_type'] = order_by_type
            
        print(f"Sending request to {self.BASE_URL}/balance")
        print(f"Headers: {self._session.headers}")
        print(f"Params: {params}")
        
        response = self._session.get(
            f'{self.BASE_URL}/balance',
            params=params
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
        if not response.ok:
            raise SMSGatewayError(
                f'API request failed with status: {response.status_code}'
            )
            
        try:
            return BalanceResponse.parse_obj(response.json())
        except Exception as e:
            raise SMSGatewayError(f'Failed to parse response: {e}')

    def get_sender_names(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
        order_by: Optional[str] = None,
        order_by_type: Optional[str] = None
    ) -> SenderNamesResponse:
        """Get list of sender names.
        
        Args:
            page: Page number for pagination
            per_page: Number of items per page
            order_by: Sort field
            order_by_type: Sort direction (asc or desc)
        
        Returns:
            SenderNamesResponse object containing list of sender names
        
        Raises:
            SMSGatewayError: If the API request fails
        """
        params = {}
        if page is not None:
            params['page'] = page
        if per_page is not None:
            params['per_page'] = per_page
        if order_by:
            params['order_by'] = order_by
        if order_by_type:
            params['order_by_type'] = order_by_type
            
        print(f"Sending request to {self.BASE_URL}/senders")
        print(f"Headers: {self._session.headers}")
        print(f"Params: {params}")
        
        response = self._session.get(
            f'{self.BASE_URL}/senders',
            params=params
        )
        
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {response.headers}")
        print(f"Response text: {response.text}")
        
        if not response.ok:
            raise SMSGatewayError(
                f'API request failed with status: {response.status_code}'
            )
            
        try:
            return SenderNamesResponse.parse_obj(response.json())
        except Exception as e:
            raise SMSGatewayError(f'Failed to parse response: {e}')

    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._session.close()
