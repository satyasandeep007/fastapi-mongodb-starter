from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.config import settings
from app.core.security import verify_password, create_access_token
from app.database.mongodb import get_database
from app.models.token import Token

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    db=Depends(get_database), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = await db.users.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user["_id"])}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
