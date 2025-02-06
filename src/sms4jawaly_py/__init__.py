"""
مكتبة بايثون لبوابة الرسائل 4jawaly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

مكتبة بايثون لارسال رسائل SMS من خلال بوابة الرسائل 4jawaly.

الاستخدام الأساسي:

    >>> from fourjawaly_sms import SMS4JawalyClient
    >>> client = SMS4JawalyClient('your_api_key', 'your_api_secret', 'YOUR_SENDER_NAME')
    >>> response = client.send_single_sms('966500000000', 'Hello from Python!')
    >>> response.success
    True
"""

__version__ = "1.0.0"

import os
import logging

# إعداد التسجيل
logging.basicConfig(
    level=os.environ.get("SMS4JAWALY_LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# تصدير الفئات والوظائف الرئيسية
from .sms_gateway import SMS4JawalyClient
from .models import SMSRequest, SMSResponse, BalanceResponse, SenderNamesResponse

__all__ = [
    "SMS4JawalyClient",
    "SMSRequest",
    "SMSResponse",
    "BalanceResponse",
    "SenderNamesResponse"
]
