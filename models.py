from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum, Text, Date, ForeignKey
from sqlalchemy.sql import func
from database import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    user = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(100), nullable=True)
    hashed_password = Column(String(255), nullable=False)
    role = Column(Enum(RoleEnum), default=RoleEnum.user, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    # ──=== 新增這一行：預設為未付費 ===──
    is_paid = Column(Boolean, default=False)

class ServiceItem(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), index=True, nullable=False) # 服務類別
    name = Column(String(100), nullable=False)                # 服務名稱/專案
    merchant_name = Column(String(100), nullable=True)        # 商戶名稱 (新增)
    description = Column(Text, nullable=True)                 # 服務說明
    published_date = Column(Date, nullable=False)             # 上架/建立日期
    has_uploaded = Column(Boolean, default=False)             # 資料是否已上傳 (新增)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    #user_id = Column(Integer, ForeignKey("users.id"), nullable=True) # ─── 2. 新增綁定使用者的外鍵 ───
    user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
