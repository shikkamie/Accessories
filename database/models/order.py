from datetime import datetime

from sqlalchemy import Column, Enum, Integer, String, Text, DateTime, ForeignKey, Boolean, BigInteger
from sqlalchemy.types import DECIMAL as Decimal
from base import Base




class Cart(Base):
    __tablename__ = 'cart'
    user_id = Column(ForeignKey('users.telegram_id'), primary_key=True, nullable=False)
    quantity = Column(Integer, default=0)
    updated_at = Column(DateTime, default=datetime.utcnow)

class CartItem(Base):
    __tablename__ = 'cart_items'


    cart_id = Column(ForeignKey('cart.user_id'), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False, primary_key=True)
    quantity = Column(Integer, default=1)
    price_at_time = Column(Decimal(10, 2), nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)




class OrderStatus(Enum):
    CREATED = "Создан"
    IN_PROGRESS = "В процессе"
    IN_DELIVERY = "В доставке"
    DELIVERED = "Доставлен"

class Order(Base):
    __tablename__ = 'orders'


    order_number = Column(String(50), primary_key=True, index=True)
    user_id = Column(ForeignKey('users.id'), nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.CREATED, index=True)
    delivery_address = Column(Text, nullable=False)
    phone = Column(String(20), nullable=False)
    notes = Column(Text, nullable=True)
    bonus_used = Column(Integer, default=0)
    total_amount = Column(Decimal(10, 2), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class OrderItem(Base):
    __tablename__ = 'order_items'


    order_id = Column(ForeignKey('order.order_number'), primary_key=True, nullable=False)
    product_id = Column(ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    price_at_time = Column(Decimal(10, 2), nullable=False)
    product_name = Column(String, nullable=False)