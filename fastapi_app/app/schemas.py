from pydantic import BaseModel, EmailStr
from typing import Optional

# Users (Postgres)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

class User(UserCreate):
    id: int

# Products (MySQL)
class ProductCreate(BaseModel):
    name: str
    price: float

class Product(ProductCreate):
    id: int
