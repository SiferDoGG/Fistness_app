from fastapi import APIRouter, Depends

from dependencies.auth import get_current_user
from models.user import User
from schemas.user import UserRead

router = APIRouter(prefix="/users", tags=["users"])


@router.get(
    "/me",
    summary="Получить информацию о текущем пользователе",
    description="Возвращает информацию о текущем вошедшем пользователе",
    response_model=UserRead,
)
async def get_user(curr_user: User = Depends(get_current_user)):
    return curr_user
