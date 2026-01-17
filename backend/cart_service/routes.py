from fastapi import APIRouter, Depends, HTTPException
from database import cart_collection
from schemas import CartItem
from auth import get_current_user
from utils import get_product
from bson import ObjectId

router = APIRouter(prefix="/cart", tags=["Cart"])

def serialize(item):
    item["_id"] = str(item["_id"])
    return item


@router.post("/add")
def add_to_cart(item: CartItem, user=Depends(get_current_user)):
    product = get_product(item.product_id)

    if item.quantity > product["stock"]:
        raise HTTPException(400, "Not enough stock")

    cart_item = cart_collection.find_one({"user": user["sub"], "product_id": item.product_id})

    if cart_item:
        # Update quantity
        new_qty = cart_item["quantity"] + item.quantity
        if new_qty > product["stock"]:
            raise HTTPException(400, "Not enough stock")
        cart_collection.update_one(
            {"_id": cart_item["_id"]}, {"$set": {"quantity": new_qty}}
        )
    else:
        cart_collection.insert_one({
            "user": user["sub"],
            "product_id": item.product_id,
            "quantity": item.quantity,
            "price": product["price"]
        })

    return {"msg": "Added to cart"}


@router.get("/")
def get_cart(user=Depends(get_current_user)):
    items = list(cart_collection.find({"user": user["sub"]}))
    total = sum(i["price"] * i["quantity"] for i in items)
    for i in items:
        i["_id"] = str(i["_id"])
        i["total"] = i["price"] * i["quantity"]
    return {"items": items, "total": total}


@router.put("/update")
def update_cart(item: CartItem, user=Depends(get_current_user)):
    product = get_product(item.product_id)
    if item.quantity > product["stock"]:
        raise HTTPException(400, "Not enough stock")
    cart_collection.update_one(
        {"user": user["sub"], "product_id": item.product_id},
        {"$set": {"quantity": item.quantity, "price": product["price"]}}
    )
    return {"msg": "Cart updated"}


@router.delete("/remove/{product_id}")
def remove_from_cart(product_id: str, user=Depends(get_current_user)):
    cart_collection.delete_one({"user": user["sub"], "product_id": product_id})
    return {"msg": "Removed from cart"}
