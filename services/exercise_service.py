from repositories.exercise_repo import (
    create_exercise,
    get_exercise_by_id,
    get_exercise_by_name,
    get_exercises,
)
from fastapi import HTTPException


async def create_exercise_service(db, data):
    exercise = await get_exercise_by_name(db, data.name)
    if exercise:
        raise HTTPException(
            status_code=400, detail="Exercise with this name already exists"
        )
    return await create_exercise(db, data)


async def get_exercises_service(db):
    return await get_exercises(db)


async def get_exercise_service(db, exercise_id):
    result = await get_exercise_by_id(db, exercise_id)

    if not result:
        raise HTTPException(status_code=404, detail="Exercise not found")

    return result
