from fastapi import APIRouter
from app.routes.endpoints.user import router as user_router
from app.routes.endpoints.order import router as order_router

router = APIRouter()

# Group routers by category with their specific tags and prefixes
router_config = [
    {
        "router": user_router,
        "prefix": "/users",
        "tags": ["users"]
    },
    {
        "router": order_router,
        "prefix": "/orders",
        "tags": ["orders"]
    }
]

# Include routers with their specific configurations
for config in router_config:
    router.include_router(
        config["router"],
        prefix=config["prefix"],
        tags=config["tags"]
    )