from sqlalchemy import Column, Enum, Integer, String, Text, DateTime, ForeignKey, Boolean, BigInteger
from base import Base
from datetime import datetime




class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(BigInteger, primary_key=True, index=True, nullable=False)
    username = Column(String(50), index=True, nullable=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    phone = Column(String(20), nullable=True)
    email = Column(String(100), nullable=True)
    delivery_Address = Column(String(255), nullable=True)
    bonus_balance = Column(Integer, default=0)
    referral_code = Column(String(50), unique=True)
    referred_by = Column(ForeignKey('users.telegram_id'), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
