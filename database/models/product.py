from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
    Boolean,
)
from sqlalchemy.types import DECIMAL as Decimal

from base import Base
from datetime import datetime


class Category(Base):
    __tablename__ = "category"

    name = Column(String(100), primary_key=True, index=True, unique=True)
    description = Column(Text, nullable=True)
    is_active = Column(Boolean, default=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), index=True)
    description = Column(Text, nullable=False)
    price = Column(Decimal(10, 2), nullable=False)
    discount_price = Column(Decimal(10, 2), nullable=True)
    category_id = Column(ForeignKey("category.name"), nullable=False)
    is_active = Column(Boolean, default=True)
    telegram_file_id = Column(String(255), nullable=True)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(ForeignKey("products.id"), primary_key=True, nullable=False)
    image_url = Column(String(255), nullable=False)
    telegram_file_id = Column(String(255), nullable=True)
    is_main = Column(Boolean, default=False)
    sort_order = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
