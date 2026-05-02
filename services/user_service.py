from repositories.user_repo import get_user_by_email, create_user
from core.security import hash_password, verify_password
from fastapi import HTTPException


async def register_user(db, email: str, password: str):
    existing_user = await get_user_by_email(db, email)

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = hash_password(password)

    return await create_user(db, email, hashed)


async def authenticate_user(db, email: str, password: str):
    user = await get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return user
