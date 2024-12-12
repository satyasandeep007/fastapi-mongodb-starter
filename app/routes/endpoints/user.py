from typing import List
from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.security import get_password_hash
from app.core.deps import get_current_active_user, get_current_active_superuser
from app.database.mongodb import get_database
from app.models.user import UserCreate, UserResponse, UserInDB, UserUpdate
from bson import ObjectId

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def create_user(user_in: UserCreate, db=Depends(get_database)):
    user = await db.users.find_one({"email": user_in.email})
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )

    user_doc = UserInDB(
        **user_in.dict(), hashed_password=get_password_hash(user_in.password)
    ).dict(by_alias=True)

    await db.users.insert_one(user_doc)
    return user_doc


@router.get("/me", response_model=UserResponse)
async def read_user_me(current_user: UserInDB = Depends(get_current_active_user)):
    return current_user


@router.get("/{user_id}", response_model=UserResponse)
async def read_user_by_id(
    user_id: str,
    current_user: UserInDB = Depends(get_current_active_user),
    db=Depends(get_database),
):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/", response_model=List[UserResponse])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    current_user: UserInDB = Depends(get_current_active_superuser),
    db=Depends(get_database),
):
    users = await db.users.find().skip(skip).limit(limit).to_list(length=limit)
    return users
