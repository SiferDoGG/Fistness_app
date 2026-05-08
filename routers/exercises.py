from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies.db import get_db
from schemas.exercise import ExerciseCreate, ExerciseRead
from services.exercise_service import create_exercise_service, get_exercises_service

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get(
    "",
    summary="Получить список упражнений",
    description="Возвращает список доступных упражнений",
    response_model=List[ExerciseRead],
)
async def get_exercises(db: AsyncSession = Depends(get_db)):
    return await get_exercises_service(db)


@router.post(
    "",
    summary="Создать новое упражнение",
    description="Создаёт новое упражнение в системе",
    response_model=ExerciseRead,
)
async def create_exercise(db: AsyncSession = Depends(get_db)):
    pass


@router.get(
    "/{id}",
    summary="Получить информацию об упражнении",
    description="Возвращает информацию об указанном упражнении",
)
async def get_exercise(id: int):
    pass
