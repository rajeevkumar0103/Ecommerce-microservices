import requests
from fastapi import HTTPException

CART_SERVICE_URL = "http://localhost:8002/cart"
PRODUCT_SERVICE_URL = "http://localhost:8001/products"

def get_cart_items(token: str):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{CART_SERVICE_URL}/", headers=headers)
    if response.status_code != 200:
        raise HTTPException(400, "Cannot fetch cart")
    return response.json()["items"]

def deduct_stock(product_id: str, quantity: int):
    headers = {"Authorization": "Bearer ADMIN_JWT_TOKEN"}  # Replace with admin token
    response = requests.put(
        f"{PRODUCT_SERVICE_URL}/{product_id}",
        json={"stock_deduction": quantity},  # This endpoint we need in Product Service
        headers=headers
    )
    if response.status_code != 200:
        raise HTTPException(400, "Cannot update product stock")
