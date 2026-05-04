from fastapi import APIRouter, Depends

from schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from dependencies.db import get_db
from schemas.token import LoginRequest, LogoutRequest, RefreshRequest, TokenPair
from schemas.user import UserRead
from services import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/signup",
    response_model=UserRead,
    summary="Регистрация пользователя",
    description="Создаёт нового пользователя в системе",
)
async def signup(payload: UserCreate, db: AsyncSession = Depends(get_db)):
    return await auth_service.signup(
        db,
        username=payload.username,
        email=payload.email,
        password=payload.password,
    )


@router.post(
    "/login",
    response_model=TokenPair,
    summary="Авторизация пользователя",
    description="Проверяет учетные данные и возвращает токен доступа",
)
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db)):
    return await auth_service.login(db, email=payload.email, password=payload.password)


@router.post(
    "/refresh",
    response_model=TokenPair,
    summary="Обновление токена доступа",
    description="Использует рефреш токен для получения нового токена доступа",
)
async def refresh(payload: RefreshRequest, db: AsyncSession = Depends(get_db)):
    return await auth_service.refresh(db, refresh_token=payload.refresh_token)


@router.post(
    "/logout",
    summary="Выход из системы",
    description="Завершает сессию пользователя",
)
async def logout(payload: LogoutRequest, db: AsyncSession = Depends(get_db)):
    return await auth_service.logout(db, refresh_token=payload.refresh_token)
