from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth import get_current_user
from database import get_db
from models import Order
from schemas import OrderResponse
from utils import get_cart_items, deduct_stock
import json

router = APIRouter(prefix="/orders", tags=["Orders"])

@router.post("/checkout", response_model=OrderResponse)
def checkout(user=Depends(get_current_user), db: Session = Depends(get_db)):
    token = ""  # Use request JWT token here
    cart_items = get_cart_items(token)

    if not cart_items:
        raise HTTPException(400, "Cart is empty")

    total = 0
    for item in cart_items:
        total += item["price"] * item["quantity"]
        deduct_stock(item["product_id"], item["quantity"])

    order = Order(
        user=user["sub"],
        items=json.dumps(cart_items),
        total_amount=total,
        status="PLACED"
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    order_dict = {
        "id": order.id,
        "user": order.user,
        "items": cart_items,
        "total_amount": total,
        "status": order.status,
        "created_at": str(order.created_at)
    }

    return order_dict


@router.get("/", response_model=list[OrderResponse])
def get_orders(user=Depends(get_current_user), db: Session = Depends(get_db)):
    orders = db.query(Order).filter(Order.user == user["sub"]).all()
    result = []
    for o in orders:
        result.append({
            "id": o.id,
            "user": o.user,
            "items": json.loads(o.items),
            "total_amount": o.total_amount,
            "status": o.status,
            "created_at": str(o.created_at)
        })
    return result
