from pydantic import BaseModel

class CartItem(BaseModel):
    product_id: str
    quantity: int

class CartResponse(BaseModel):
    product_id: str
    quantity: int
    price: float
    total: float
