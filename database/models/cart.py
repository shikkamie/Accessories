from sqlalchemy import (
    Column,
    Integer,
    DateTime,
    ForeignKey,
)
from sqlalchemy.types import DECIMAL as Decimal

from base import Base
from datetime import datetime


class Cart(Base):
    __tablename__ = "cart"
    user_id = Column(ForeignKey("users.telegram_id"), primary_key=True, nullable=False)
    quantity = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow)


class CartItem(Base):
    __tablename__ = "cart_items"

    cart_id = Column(ForeignKey("cart.user_id"), primary_key=True, nullable=False)
    product_id = Column(ForeignKey("products.id"), nullable=False, primary_key=True)
    quantity = Column(Integer, default=1)
    price_at_time = Column(Decimal(10, 2), nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)
