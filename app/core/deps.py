from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.core.config import settings
from app.database.mongodb import get_database
from app.models.token import TokenPayload
from app.models.user import UserInDB
from datetime import datetime
from bson import ObjectId

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db=Depends(get_database)
) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
        if token_data.sub is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = await db.users.find_one({"_id": ObjectId(token_data.sub)})
    if user is None:
        raise credentials_exception
    return UserInDB(**user)


async def get_current_active_user(
    current_user: UserInDB = Depends(get_current_user),
) -> UserInDB:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


async def get_current_active_superuser(
    current_user: UserInDB = Depends(get_current_user),
) -> UserInDB:
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
