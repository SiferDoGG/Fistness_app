from fastapi import APIRouter

from .auth import router as auth_router
from .users import router as users_router
from .exercises import router as exercises_router
from .workouts import router as workouts_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(users_router)
router.include_router(exercises_router)
router.include_router(workouts_router)
