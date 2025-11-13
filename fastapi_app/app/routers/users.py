from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas import User, UserCreate
from .. import crud

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=User)
async def create(user: UserCreate):
    created = await crud.create_user(user)
    return created

@router.get("/", response_model=List[User])
async def list_all():
    return await crud.list_users()

@router.get("/{user_id}", response_model=User)
async def get_one(user_id: int):
    user = await crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update(user_id: int, payload: UserCreate):
    return await crud.update_user(user_id, payload)

@router.delete("/{user_id}")
async def delete(user_id: int):
    return await crud.delete_user(user_id)
