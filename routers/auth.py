from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post(
    "/signup",
    summary="Регистрация пользователя",
    description="Создаёт нового пользователя в системе",
)
async def signup():
    pass


@router.post(
    "/login",
    summary="Авторизация пользователя",
    description="Проверяет учетные данные и возвращает токен доступа",
)
async def login():
    pass


@router.post(
    "/refresh",
    summary="Обновление токена доступа",
    description="Использует рефреш токен для получения нового токена доступа",
)
async def refresh():
    pass


@router.post(
    "/logout",
    summary="Выход из системы",
    description="Завершает сессию пользователя",
)
async def logout():
    pass
