from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class ErrorNumber(BaseModel):
    """نموذج لرقم به خطأ"""
    number: str
    country: Optional[str] = None
    error: str

class MessageRequest(BaseModel):
    """نموذج لطلب إرسال الرسالة"""
    text: str
    numbers: List[str]
    sender: str

class MessageResponse(BaseModel):
    """نموذج للرد على الرسالة"""
    inserted_numbers: int
    message: Dict[str, Any]
    error_numbers: Optional[List[ErrorNumber]] = None
    no_package: Optional[List[str]] = None
    has_more_iso_code: Optional[List[str]] = None

class SMSRequest(BaseModel):
    """نموذج لطلب إرسال الرسائل"""
    messages: List[MessageRequest]

class SMSResponse(BaseModel):
    """نموذج للرد على طلب إرسال الرسائل"""
    job_id: str
    messages: List[MessageResponse]
    code: int
    message: str
    success: bool = True
    total_success: int = 0
    total_failed: int = 0

class Package(BaseModel):
    """نموذج لباقة الرسائل"""
    id: int
    package_points: int = Field(alias='package_points')
    current_points: int = Field(alias='current_points')
    expire_at: str = Field(alias='expire_at')
    is_active: bool = Field(alias='is_active')

class BalanceResponse(BaseModel):
    """نموذج للرد على طلب الرصيد"""
    balance: float
    packages: Optional[List[Package]] = None

class SenderName(BaseModel):
    """نموذج لاسم المرسل"""
    id: int
    name: str
    status: str
    note: Optional[str] = None
    created_at: str = Field(alias='created_at')
    updated_at: str = Field(alias='updated_at')

class SenderNamesResponse(BaseModel):
    """نموذج للرد على طلب أسماء المرسلين"""
    success: bool
    data: List[SenderName]
    total: int
