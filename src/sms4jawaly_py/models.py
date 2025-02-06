from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class ErrorNumber(BaseModel):
    """نموذج لرقم به خطأ"""
    number: str
    error: str

class Message(BaseModel):
    """نموذج للرسالة"""
    text: str
    numbers: List[str]
    sender: str
    err_text: Optional[str] = None
    error_numbers: Optional[List[ErrorNumber]] = None

class SMSRequest(BaseModel):
    """نموذج لطلب إرسال الرسائل"""
    messages: List[Message]

class SMSResponse(BaseModel):
    """نموذج للرد على طلب إرسال الرسائل"""
    success: bool = True
    total_success: int = 0
    total_failed: int = 0
    job_id: Optional[str] = None
    messages: Optional[List[Message]] = None
    errors: Optional[Dict[str, List[str]]] = None

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
