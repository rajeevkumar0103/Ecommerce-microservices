import requests
from fastapi import HTTPException

PRODUCT_SERVICE_URL = "http://localhost:8001/products"

def get_product(product_id: str):
    response = requests.get(f"{PRODUCT_SERVICE_URL}/{product_id}")
    if response.status_code != 200:
        raise HTTPException(404, "Product not found")
    return response.json()
