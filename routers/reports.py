from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get(
    "/summary",
    summary="Получить сводный отчёт",
    description="Возвращает сводную информацию о тренировках",
)
async def get_summary_report():
    pass


@router.get(
    "/progress",
    summary="Получить отчёт о прогрессе",
    description="Возвращает информацию о прогрессе пользователя",
)
async def get_progress_report():
    pass
