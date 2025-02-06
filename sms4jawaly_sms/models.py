from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class SMSRequest(BaseModel):
    """Request model for sending SMS."""
    numbers: List[str]
    message: str
    sender: str

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
