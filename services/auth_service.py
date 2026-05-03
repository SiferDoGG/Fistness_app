from repositories.user_repo import get_user_by_email, create_user
from core.security import (
    create_refresh_token,
    hash_password,
    verify_password,
    create_access_token,
)
from fastapi import HTTPException


async def signup(db, username: str, email: str, password: str):
    user = await get_user_by_email(db, email)

    if user:
        raise HTTPException(status_code=400, detail="User exists")

    hashed = hash_password(password)

    return await create_user(db, username, email, hashed)


async def login(db, email: str, password: str):
    user = await get_user_by_email(db, email)

    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    await create_refresh_token(db, refresh_token, user.id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
