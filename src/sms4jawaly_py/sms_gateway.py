import base64
import logging
import requests
from typing import List, Dict, Any, Optional
from .models import (
    SMSRequest, SMSResponse, BalanceResponse,
    SenderNamesResponse, MessageRequest
)

logger = logging.getLogger(__name__)

class SMSGatewayError(Exception):
    """خطأ في بوابة الرسائل"""
    pass

class SMS4JawalyClient:
    """عميل بوابة الرسائل"""
    
    def __init__(
        self,
        api_key: str,
        api_secret: str,
        sender: str,
        base_url: str = "https://api-sms.4jawaly.com/api/v1/"
    ):
        """تهيئة عميل بوابة الرسائل
        
        Args:
            api_key: مفتاح API
            api_secret: كلمة سر API
            sender: اسم المرسل
            base_url: عنوان API الأساسي
        """
        self.base_url = base_url.rstrip("/") + "/"
        self.sender = sender
        
        # إنشاء رأس المصادقة
        credentials = f"{api_key}:{api_secret}"
        auth_hash = base64.b64encode(credentials.encode()).decode()
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Basic {auth_hash}"
        }

    def _make_request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        params: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """إرسال طلب إلى API
        
        Args:
            method: طريقة الطلب (GET, POST, etc.)
            endpoint: نقطة النهاية
            data: بيانات الطلب
            params: معلمات الطلب
            
        Returns:
            Dict[str, Any]: استجابة API
            
        Raises:
            SMSGatewayError: عند فشل الطلب
        """
        url = self.base_url + endpoint.lstrip("/")
        
        logger.info(f"Sending request to {url}")
        logger.debug(f"Headers: {self.headers}")
        if data:
            logger.debug(f"Data: {data}")
        if params:
            logger.debug(f"Params: {params}")
            
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data,
                params=params
            )
            
            logger.debug(f"Response status: {response.status_code}")
            logger.debug(f"Response headers: {response.headers}")
            logger.debug(f"Response text: {response.text}")
            
            if response.status_code >= 400:
                raise SMSGatewayError(
                    f"API request failed with status: {response.status_code}"
                )
                
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise SMSGatewayError(f"Failed to make request: {e}")
            
    def send_sms(self, numbers: List[str], message: str) -> SMSResponse:
        """إرسال رسالة SMS
        
        Args:
            numbers: قائمة بأرقام الهواتف
            message: نص الرسالة
            
        Returns:
            SMSResponse: نتيجة الإرسال
            
        Raises:
            SMSGatewayError: عند فشل الإرسال
        """
        try:
            request = SMSRequest(
                messages=[
                    MessageRequest(
                        text=message,
                        numbers=numbers,
                        sender=self.sender
                    )
                ]
            )
            
            response = self._make_request(
                method="POST",
                endpoint="account/area/sms/send",
                data=request.dict()
            )
            
            return SMSResponse.parse_obj(response)
            
        except Exception as e:
            raise SMSGatewayError(f"Failed to parse response: {e}")
            
    def send_single_sms(self, number: str, message: str) -> SMSResponse:
        """إرسال رسالة SMS لرقم واحد
        
        Args:
            number: رقم الهاتف
            message: نص الرسالة
            
        Returns:
            SMSResponse: نتيجة الإرسال
        """
        return self.send_sms([number], message)
        
    def get_balance(self) -> BalanceResponse:
        """جلب رصيد الحساب
        
        Returns:
            BalanceResponse: معلومات الرصيد
            
        Raises:
            SMSGatewayError: عند فشل جلب الرصيد
        """
        try:
            params = {
                "is_active": 1,
                "order_by": "id",
                "order_by_type": "desc",
                "page": 1,
                "page_size": 10,
                "return_collection": 1
            }
            
            response = self._make_request(
                method="GET",
                endpoint="account/area/me/packages",
                params=params
            )
            
            return BalanceResponse.parse_obj(response)
            
        except Exception as e:
            raise SMSGatewayError(f"Failed to parse response: {e}")
            
    def get_sender_names(self) -> SenderNamesResponse:
        """جلب أسماء المرسلين
        
        Returns:
            SenderNamesResponse: قائمة بأسماء المرسلين
            
        Raises:
            SMSGatewayError: عند فشل جلب الأسماء
        """
        try:
            params = {
                "page_size": 10,
                "page": 1,
                "status": 1,
                "sender_name": "",
                "is_ad": "",
                "return_collection": 1
            }
            
            response = self._make_request(
                method="GET",
                endpoint="account/area/senders",
                params=params
            )
            
            return SenderNamesResponse.parse_obj(response)
            
        except Exception as e:
            raise SMSGatewayError(f"Failed to parse response: {e}")
