from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.token import RefreshToken


async def create_refresh_token(db: AsyncSession, token: str, user_id: int):
    obj = RefreshToken(token=token, user_id=user_id)
    db.add(obj)
    await db.commit()
    return obj


async def get_refresh_token(db: AsyncSession, token: str):
    result = await db.execute(select(RefreshToken).where(RefreshToken.token == token))
    return result.scalar_one_or_none()


async def delete_refresh_token(db: AsyncSession, token: str):
    obj = await get_refresh_token(db, token)
    if obj:
        await db.delete(obj)
        await db.commit()
