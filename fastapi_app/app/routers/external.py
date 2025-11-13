from fastapi import APIRouter
from ..external_api import fetch_sample

router = APIRouter(prefix="/external", tags=["external"])

@router.get("/jsonplaceholder")
async def jsonplaceholder_proxy():
    return await fetch_sample()
