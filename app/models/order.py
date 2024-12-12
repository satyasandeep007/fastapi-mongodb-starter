from datetime import datetime
from typing import Optional, Annotated
from pydantic import BaseModel, Field, BeforeValidator
from bson import ObjectId

# Custom type for ObjectId fields
PyObjectId = Annotated[str, BeforeValidator(str)]

class OrderModel(BaseModel):
    id: PyObjectId = Field(default_factory=lambda: str(ObjectId()), alias="_id")
    user_id: PyObjectId
    total_amount: float
    status: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "user_id": "507f1f77bcf86cd799439011",
                "total_amount": 99.99,
                "status": "pending"
            }
        }

class OrderCreate(BaseModel):
    user_id: PyObjectId
    total_amount: float
    status: str

class OrderUpdate(BaseModel):
    total_amount: Optional[float] = None
    status: Optional[str] = None

class OrderResponse(BaseModel):
    id: PyObjectId = Field(alias="_id")
    user_id: PyObjectId
    total_amount: float
    status: str
    created_at: datetime

    class Config:
        populate_by_name = True