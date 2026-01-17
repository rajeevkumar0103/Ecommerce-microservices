from fastapi import APIRouter, Depends, HTTPException
from database import product_collection
from schemas import ProductCreate
from bson import ObjectId
from cache import get_cache, set_cache, clear_cache
from auth import admin_only

router = APIRouter(prefix="/products", tags=["Products"])

def serialize(product):
    product["_id"] = str(product["_id"])
    return product


@router.post("/", dependencies=[Depends(admin_only)])
def create_product(product: ProductCreate):
    result = product_collection.insert_one(product.dict())
    clear_cache()
    return {"id": str(result.inserted_id)}


@router.get("/")
def list_products(page: int = 1, limit: int = 10):
    cache_key = f"products:{page}:{limit}"
    cached = get_cache(cache_key)
    if cached:
        return {"cached": True, "data": cached}

    skip = (page - 1) * limit
    products = product_collection.find().skip(skip).limit(limit)
    data = [serialize(p) for p in products]

    set_cache(cache_key, data)
    return {"cached": False, "data": data}


@router.get("/{id}")
def get_product(id: str):
    product = product_collection.find_one({"_id": ObjectId(id)})
    if not product:
        raise HTTPException(404, "Not found")
    return serialize(product)


@router.put("/{id}", dependencies=[Depends(admin_only)])
def update_product(id: str, product: ProductCreate):
    product_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": product.dict()}
    )
    clear_cache()
    return {"msg": "Updated"}


@router.delete("/{id}", dependencies=[Depends(admin_only)])
def delete_product(id: str):
    product_collection.delete_one({"_id": ObjectId(id)})
    clear_cache()
    return {"msg": "Deleted"}
