from typing import List, Union, Optional, Dict
import requests
from .exceptions import SMSGatewayException

class SMSGateway:
    """4jawaly SMS Gateway client"""
    
    def __init__(self, api_key: str, api_secret: str, sender: str):
        """
        Initialize the SMS Gateway client
        
        Args:
            api_key: Your API key
            api_secret: Your API secret
            sender: Default sender name (must be pre-approved)
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.sender = sender
        self.base_url = 'https://api-sms.4jawaly.com/api/v1/'
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': self.api_key,
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })
    
    def send(self, numbers: Union[str, List[str]], message: str, sender: Optional[str] = None) -> Dict:
        """
        Send SMS message to one or multiple recipients
        
        Args:
            numbers: Single number or list of numbers
            message: Message content
            sender: Optional sender name (if different from default)
            
        Returns:
            Dict containing API response
            
        Raises:
            SMSGatewayException: If the API request fails
        """
        if isinstance(numbers, str):
            numbers = [numbers]
            
        data = {
            'numbers': numbers,
            'message': message,
            'sender': sender or self.sender,
        }
        
        try:
            response = self.session.post(f'{self.base_url}send', json=data)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise SMSGatewayException(f'Failed to send SMS: {str(e)}') from e
    
    def get_balance(self, is_active: Optional[int] = None,
                    order_by: Optional[str] = None,
                    order_by_type: Optional[str] = None) -> Dict:
        """
        Get account balance and package information
        
        Args:
            is_active: Filter by active packages (0 or 1)
            order_by: Sort field
            order_by_type: Sort direction (asc or desc)
            
        Returns:
            Dict containing balance information
            
        Raises:
            SMSGatewayException: If the API request fails
        """
        params = {
            'is_active': is_active,
            'order_by': order_by,
            'order_by_type': order_by_type
        }
        
        # Remove None values
        params = {k: v for k, v in params.items() if v is not None}
        
        try:
            response = self.session.get(f'{self.base_url}balance', params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise SMSGatewayException(f'Failed to get balance: {str(e)}') from e
