from pydantic import BaseModel
from typing import List, Dict

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderCreate(BaseModel):
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: int
    user: str
    items: List[Dict]
    total_amount: float
    status: str
    created_at: str
