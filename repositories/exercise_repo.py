from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.exercise import Exercise


async def get_all_exercises(db: AsyncSession):
    result = await db.execute(select(Exercise))
    return result.scalars().all()


async def get_exercise_by_id(db: AsyncSession, exercise_id: int):
    result = await db.execute(select(Exercise).where(Exercise.id == exercise_id))
    return result.scalar_one_or_none()


async def create_exercise(db: AsyncSession, name: str, description: str):
    exercise = Exercise(name=name, description=description)
    db.add(exercise)
    await db.commit()
    await db.refresh(exercise)
    return exercise
