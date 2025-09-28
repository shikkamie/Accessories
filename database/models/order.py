from datetime import datetime

from sqlalchemy import (
    Column,
    Enum,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.types import DECIMAL as Decimal
from base import Base


class OrderStatus(Enum):
    CREATED = "Создан"
    IN_PROGRESS = "В процессе"
    IN_DELIVERY = "В доставке"
    DELIVERED = "Доставлен"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_number = Column(String(50), primary_key=True, index=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.CREATED, index=True)
    delivery_address = Column(Text, nullable=False)
    phone = Column(String(20), nullable=False)
    notes = Column(Text, nullable=True)
    bonus_used = Column(Integer, default=0)
    total_amount = Column(Decimal(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(
        ForeignKey("order.order_number"), primary_key=True, nullable=False
    )
    product_id = Column(ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    price_at_time = Column(Decimal(10, 2), nullable=False)
    product_name = Column(String, nullable=False)
