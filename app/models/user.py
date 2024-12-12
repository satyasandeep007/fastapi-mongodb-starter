from datetime import datetime
from typing import Optional
from pydantic import EmailStr, Field
from app.models.base import MongoBaseModel, PyObjectId

class UserBase(MongoBaseModel):
    email: EmailStr
    username: str
    is_active: bool = True
    is_superuser: bool = False

class UserCreate(MongoBaseModel):
    email: EmailStr
    username: str
    password: str

class UserUpdate(MongoBaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None

class UserInDB(UserBase):
    hashed_password: str

class UserResponse(UserBase):
    pass

    class Config:
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "is_active": True,
                "created_at": datetime.utcnow()
            }
        }