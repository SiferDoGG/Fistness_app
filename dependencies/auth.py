from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.security import decode_token, oauth2_scheme
from dependencies.db import get_db
from repositories.user_repo import get_user_by_id


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)
):
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")

    user_id = payload.get("sub")

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    try:
        user_id_int = int(user_id)
    except (TypeError, ValueError):
        raise HTTPException(status_code=401, detail="Invalid token payload")

    user = await get_user_by_id(db, user_id_int)

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
