from fastapi import APIRouter, HTTPException
from .repository import InseureRepository

router = APIRouter()

@router.put("/price", status_code=202)
async def insurance(data: dict):
    try:
        await InseureRepository.load_prices(data)
    except:
        raise HTTPException(status_code=400, detail="Bad request")

@router.get("/price")
async def insurances(date: str, cargo_type: str, price: float) -> float:
    try:
        return await InseureRepository.get_price(date, cargo_type, price)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))