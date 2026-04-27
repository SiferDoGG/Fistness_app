from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    description="Маршруты для управления пользователями",
)


@router.get(
    "/me",
    summary="Получить информацию о текущем пользователе",
    description="Возвращает информацию о текущем вошедших пользователе",
)
async def get_current_user():
    pass
