from repositories.user_repo import get_user_by_email, create_user
from repositories.token_repo import (
    create_refresh_token as save_refresh_token,
    delete_refresh_token,
    get_refresh_token,
)
from core.security import (
    create_refresh_token,
    decode_token,
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

    await save_refresh_token(db, refresh_token, user.id)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


async def refresh(db, refresh_token: str):
    stored_token = await get_refresh_token(db, refresh_token)

    if not stored_token:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    payload = decode_token(refresh_token)

    if not payload or not payload.get("sub"):
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = payload["sub"]

    new_access_token = create_access_token({"sub": user_id})
    new_refresh_token = create_refresh_token({"sub": user_id})

    await delete_refresh_token(db, refresh_token)
    await save_refresh_token(db, new_refresh_token, int(user_id))

    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token,
        "token_type": "bearer",
    }


async def logout(db, refresh_token: str):
    stored_token = await get_refresh_token(db, refresh_token)

    if not stored_token:
        raise HTTPException(status_code=404, detail="Refresh token not found")

    await delete_refresh_token(db, refresh_token)

    return {"message": "Logged out successfully"}
