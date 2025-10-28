from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class GroceryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    category: str = Field(..., min_length=1, max_length=50)
    purchase_date: Optional[datetime] = None
    expiry_date: datetime
    quantity: float = Field(default=1.0, gt=0)
    unit: str = Field(default="piece", max_length=20)
    price: Optional[float] = Field(default=None, ge=0)
    notes: Optional[str] = Field(default=None, max_length=500)


class GroceryCreate(GroceryBase):
    pass


class GroceryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    purchase_date: Optional[datetime] = None
    expiry_date: Optional[datetime] = None
    quantity: Optional[float] = Field(None, gt=0)
    unit: Optional[str] = Field(None, max_length=20)
    price: Optional[float] = Field(None, ge=0)
    is_expired: Optional[bool] = None
    is_notified: Optional[bool] = None
    notes: Optional[str] = Field(None, max_length=500)


class GroceryResponse(GroceryBase):
    id: int
    is_expired: bool
    is_notified: bool
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class GroceryListResponse(BaseModel):
    groceries: list[GroceryResponse]
    total: int


class OCRRequest(BaseModel):
    image_url: Optional[str] = None  # For future implementation with image URLs

