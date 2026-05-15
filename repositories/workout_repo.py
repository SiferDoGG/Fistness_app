from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from models.workout import Workout
from schemas.enum import WorkoutStatus


async def get_workouts(
    db: AsyncSession,
    limit: int = 10,
    offset: int = 0,
    status: WorkoutStatus = None,
):
    query = select(Workout)

    if status:
        query = query.where(Workout.status == status)

    query = query.limit(limit).offset(offset)

    result = await db.execute(query)

    return result.scalars().all()
