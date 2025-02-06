from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class SMSRequest(BaseModel):
    """Request model for sending SMS."""
    messages: List[str] = Field(alias='messages')
    recipients: List[str] = Field(alias='recipients')
    sender: str = Field(alias='sender')

class SMSResponse(BaseModel):
    """Response model for SMS requests."""
    success: bool
    total_success: int = Field(alias='total_success')
    total_failed: int = Field(alias='total_failed')
    job_ids: List[str] = Field(alias='job_ids')
    errors: Optional[Dict[str, List[str]]] = None

class Package(BaseModel):
    """Model for SMS package information."""
    id: int
    package_points: int = Field(alias='package_points')
    current_points: int = Field(alias='current_points')
    expire_at: str = Field(alias='expire_at')
    is_active: bool = Field(alias='is_active')

class BalanceResponse(BaseModel):
    """Response model for balance requests."""
    balance: float
    packages: Optional[List[Package]] = None

class SenderName(BaseModel):
    """Model for sender name information."""
    id: int
    name: str
    status: str
    note: Optional[str] = None
    created_at: str = Field(alias='created_at')
    updated_at: str = Field(alias='updated_at')

class SenderNamesResponse(BaseModel):
    """Response model for sender names requests."""
    success: bool
    data: List[SenderName]
    total: int
