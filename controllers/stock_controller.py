from fastapi import APIRouter

from models.stock import Stock

router = APIRouter()


@router.post("/")
async def add_stock(stock: Stock):
    await stock.save()
    return stock


@router.get("/")
async def get_stock():
    return await Stock.objects.all()
