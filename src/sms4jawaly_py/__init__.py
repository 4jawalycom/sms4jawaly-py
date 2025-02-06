"""
4jawaly SMS Gateway SDK for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Python library for sending SMS messages through the 4jawaly SMS Gateway.

Basic usage:

    >>> from fourjawaly_sms import SMS4JawalyClient
    >>> client = SMS4JawalyClient('your_api_key', 'your_api_secret', 'YOUR_SENDER_NAME')
    >>> response = client.send_single_sms('966500000000', 'Hello from 4jawaly!')
    >>> print(response.success)
    True
"""

from .sms_gateway import SMSGateway as SMS4JawalyClient
from .models import SMSResponse, BalanceResponse, SenderNamesResponse

__version__ = "1.0.0"

__all__ = [
    "SMS4JawalyClient",
    "SMSResponse",
    "BalanceResponse",
    "SenderNamesResponse"
]
