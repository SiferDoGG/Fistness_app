from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.exercise import Exercise


async def get_all_exercises(db: AsyncSession):
    result = await db.execute(select(Exercise))
    return result.scalars().all()


async def get_exercise_by_id(db: AsyncSession, exercise_id: int):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id))
    return result.scalar_one_or_none()


async def create_exercise(db: AsyncSession, exercise_data: dict):
    exercise = Exercise(**exercise_data)
    try:
        db.add(exercise)
        await db.commit()
        await db.refresh(exercise)
    except Exception:
        await db.rollback()
        raise
    return exercise


async def get_exercise_by_name(db: AsyncSession, name: str):
    result = await db.execute(select(Exercise).where(Exercise.name == name))
    return result.scalar_one_or_none()
