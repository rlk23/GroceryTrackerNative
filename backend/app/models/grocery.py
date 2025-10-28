from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from sqlalchemy.sql import func
from app.core.database import Base


class Grocery(Base):
    __tablename__ = "groceries"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    category = Column(String, nullable=False)
    purchase_date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    expiry_date = Column(DateTime(timezone=True), nullable=False)
    quantity = Column(Float, default=1.0)
    unit = Column(String, default="piece")  # piece, kg, liter, etc.
    price = Column(Float, nullable=True)
    is_expired = Column(Boolean, default=False)
    is_notified = Column(Boolean, default=False)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

