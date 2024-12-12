from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database import get_database
from app.models.order import OrderModel, OrderCreate, OrderUpdate, OrderResponse
from typing import List
from bson import ObjectId
from bson.errors import InvalidId
router = APIRouter()

@router.post("/", response_model=OrderResponse)
async def create_order(order: OrderCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(order.user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    # Check if user exists
    user = await db.users.find_one({"_id": ObjectId(order.user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    order_data = OrderModel(
        user_id=ObjectId(order.user_id),
        total_amount=order.total_amount,
        status=order.status
    )
    
    result = await db.orders.insert_one(order_data.dict(by_alias=True))
    created_order = await db.orders.find_one({"_id": result.inserted_id})
    return created_order

@router.get("/", response_model=List[OrderResponse])
async def get_orders(skip: int = 0, limit: int = 100, db: AsyncIOMotorDatabase = Depends(get_database)):
    orders = await db.orders.find().skip(skip).limit(limit).to_list(length=limit)
    return orders

@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    try:
        order = await db.orders.find_one({"_id": ObjectId(order_id)})
        if order is None:
            raise HTTPException(status_code=404, detail="Order not found")
        return order
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid order ID format")

@router.put("/{order_id}", response_model=OrderResponse)
async def update_order(order_id: str, order: OrderUpdate, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order ID")
    
    order_data = order.dict(exclude_unset=True)
    if len(order_data) >= 1:
        update_result = await db.orders.update_one(
            {"_id": ObjectId(order_id)}, {"$set": order_data}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=404, detail="Order not found")
            
    updated_order = await db.orders.find_one({"_id": ObjectId(order_id)})
    return updated_order

@router.delete("/{order_id}")
async def delete_order(order_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(order_id):
        raise HTTPException(status_code=400, detail="Invalid order ID")
    
    delete_result = await db.orders.delete_one({"_id": ObjectId(order_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return {"message": "Order deleted successfully"}