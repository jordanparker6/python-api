"""Example model definitions for SQLAlchemy's ORM system"""
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Float, Enum
from sqlalchemy.orm import relationship

from app.core.database import Base

class Customer(Base):
    __tablename__ = "customers"

    uid = Column(String, primary_key=True, index=True)
    name = Column(String, unique=True)