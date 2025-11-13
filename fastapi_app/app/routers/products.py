from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas import Product, ProductCreate
from .. import crud

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=Product)
async def create(product: ProductCreate):
    return await crud.create_product(product)

@router.get("/", response_model=List[Product])
async def list_all():
    return await crud.list_products()

@router.get("/{product_id}", response_model=Product)
async def get_one(product_id: int):
    product = await crud.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.put("/{product_id}", response_model=Product)
async def update(product_id: int, payload: ProductCreate):
    return await crud.update_product(product_id, payload)

@router.delete("/{product_id}")
async def delete(product_id: int):
    return await crud.delete_product(product_id)
