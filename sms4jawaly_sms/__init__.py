"""
4jawaly SMS Gateway SDK for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Python library for sending SMS messages through the 4jawaly SMS Gateway.

Basic usage:

    >>> from fourjawaly_sms import SMSGateway
    >>> client = SMSGateway('your_api_key', 'your_api_secret', 'YOUR_SENDER_NAME')
    >>> response = client.send_single_sms('966500000000', 'Hello from 4jawaly!')
    >>> print(response.success)
    True
"""

from .sms_gateway import SMSGateway, SMSGatewayError
from .models import SMSRequest, SMSResponse, Package, BalanceResponse

__version__ = '1.0.0'
__all__ = [
    'SMSGateway',
    'SMSGatewayError',
    'SMSRequest',
    'SMSResponse',
    'Package',
    'BalanceResponse'
]
