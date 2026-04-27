from fastapi import APIRouter

router = APIRouter(prefix="/workouts", tags=["workouts"])


@router.get(
    "",
    summary="Получить список тренировок",
    description="Возвращает список доступных тренировок",
)
async def get_workouts():
    pass


@router.post(
    "",
    summary="Создать новую тренировку",
    description="Создаёт новую тренировку в системе",
)
async def create_workout():
    pass


@router.get(
    "/{id}",
    summary="Получить информацию о тренировке",
    description="Возвращает информацию о указанной тренировке",
)
async def get_workout(id: int):
    pass


@router.patch(
    "/{id}",
    summary="Обновить информацию о тренировке",
    description="Обновляет информацию о указанной тренировке",
)
async def update_workout(id: int):
    pass


@router.delete(
    "/{id}",
    summary="Удалить тренировку",
    description="Удаляет указанную тренировку из системы",
)
async def delete_workout(id: int):
    pass
