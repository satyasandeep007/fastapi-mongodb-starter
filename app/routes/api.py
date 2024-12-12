from fastapi import APIRouter
from app.routes.endpoints import auth
from app.routes.endpoints import user
from app.routes.endpoints import order

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])

api_router.include_router(user.router, prefix="/user", tags=["user"])

api_router.include_router(order.router, prefix="/order", tags=["order"])
