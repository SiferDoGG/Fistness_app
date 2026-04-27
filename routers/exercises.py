from fastapi import APIRouter

router = APIRouter(prefix="/exercises", tags=["exercises"])


@router.get(
    "",
    summary="Получить список упражнений",
    description="Возвращает список доступных упражнений",
)
async def get_exercises():
    pass


@router.post(
    "",
    summary="Создать новое упражнение",
    description="Создаёт новое упражнение в системе",
)
async def create_exercise():
    pass


@router.get(
    "/{id}",
    summary="Получить информацию об упражнении",
    description="Возвращает информацию об указанном упражнении",
)
async def get_exercise(id: int):
    pass
