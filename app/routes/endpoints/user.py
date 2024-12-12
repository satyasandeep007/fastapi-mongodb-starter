from fastapi import APIRouter, HTTPException, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.database import get_database
from app.models.user import UserModel, UserCreate, UserUpdate, UserResponse
from typing import List
from bson import ObjectId
from passlib.context import CryptContext
from bson.errors import InvalidId

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncIOMotorDatabase = Depends(get_database)):
    # Check if email already exists
    if await db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create user model
    user_data = UserModel(
        email=user.email,
        username=user.username,
        hashed_password=pwd_context.hash(user.password)
    )
    
    result = await db.users.insert_one(user_data.dict(by_alias=True))
    created_user = await db.users.find_one({"_id": result.inserted_id})
    return created_user

@router.get("/", response_model=List[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db: AsyncIOMotorDatabase = Depends(get_database)):
    print("get_users endpoint called")
    users = await db.users.find().skip(skip).limit(limit).to_list(length=limit)
    print(f"Found {len(users)} users")
    return users

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    try:
        user = await db.users.find_one({"_id": ObjectId(user_id)})
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user: UserUpdate, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    user_data = user.dict(exclude_unset=True)
    if "password" in user_data:
        user_data["hashed_password"] = pwd_context.hash(user_data.pop("password"))
    
    if len(user_data) >= 1:
        update_result = await db.users.update_one(
            {"_id": ObjectId(user_id)}, {"$set": user_data}
        )
        if update_result.modified_count == 0:
            raise HTTPException(status_code=404, detail="User not found")
            
    updated_user = await db.users.find_one({"_id": ObjectId(user_id)})
    return updated_user

@router.delete("/{user_id}")
async def delete_user(user_id: str, db: AsyncIOMotorDatabase = Depends(get_database)):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Invalid user ID")
    
    delete_result = await db.users.delete_one({"_id": ObjectId(user_id)})
    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {"message": "User deleted successfully"}