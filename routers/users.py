from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/me",
    summary="Получить информацию о текущем пользователе",
    description="Возвращает информацию о текущем вошедшем пользователе",
)
async def get_user():
    pass
