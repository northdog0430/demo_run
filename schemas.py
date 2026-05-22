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
    # ──=== 新增這一行 ===──
    is_paid: bool = False


class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    password: Optional[str] = None
    role: Optional[RoleEnum] = None
    is_active: Optional[bool] = None
    # ──=== 新增這一行 ===──
    is_paid: Optional[bool] = None

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
    user_id: Optional[int] = None        # ─── 新增這行，指派專案給特定 User ID ───

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
