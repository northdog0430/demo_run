from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime, date
from models import RoleEnum

class Token(BaseModel):
    access_token: str
    token_type: str

class LoginRequest(BaseModel):
    username: str
    password: str

# --- User Schemas ---
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    role: RoleEnum = RoleEnum.user
    is_active: bool = True

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    role: Optional[RoleEnum] = None
    is_active: Optional[bool] = None

class UserResponse(UserBase):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True

# --- ServiceItem Schemas ---
class ServiceItemBase(BaseModel):
    category: str
    name: str
    merchant_name: Optional[str] = None  # 新增
    description: Optional[str] = None
    published_date: date
    has_uploaded: bool = False           # 新增

class ServiceItemCreate(ServiceItemBase):
    pass

class ServiceItemUpdate(BaseModel):
    category: Optional[str] = None
    name: Optional[str] = None
    merchant_name: Optional[str] = None
    description: Optional[str] = None
    published_date: Optional[date] = None
    has_uploaded: Optional[bool] = None

class ServiceItemResponse(ServiceItemBase):
    id: int
    created_at: Optional[datetime] = None
    class Config:
        from_attributes = True
