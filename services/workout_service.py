from repositories.workout_repo import get_workouts
from schemas.enum import WorkoutStatus


async def get_workouts_service(
    db,
    limit: int = 10,
    offset: int = 0,
    status: WorkoutStatus = None,
):

    return await get_workouts(db, limit, offset, status)
