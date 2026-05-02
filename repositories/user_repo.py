from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.user import User


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def create_user(db: AsyncSession, email: str, password: str):
    user = User(email=email, password=password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
