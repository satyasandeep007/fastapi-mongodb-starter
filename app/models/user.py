from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, EmailStr, Field, BeforeValidator
from bson import ObjectId

# Custom type for ObjectId fields
PyObjectId = Annotated[str, BeforeValidator(str)]

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    email: EmailStr
    username: str
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "email": "user@example.com",
                "username": "johndoe",
                "hashed_password": "hashedpass123",
                "is_active": True
            }
        }

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None

class UserResponse(BaseModel):
    id: PyObjectId = Field(alias="_id")
    email: EmailStr
    username: str
    is_active: bool
    created_at: Optional[datetime] = None

    class Config:
        populate_by_name = True