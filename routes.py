from fastapi import APIRouter

from controllers import stock_controller as stock

router = APIRouter()

router.include_router(stock.router, prefix="/stocks")
