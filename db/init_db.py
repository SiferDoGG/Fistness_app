from db.base import Base
from db.session import engine

# Импорты моделей обязательны, чтобы SQLAlchemy зарегистрировал их в metadata
from models.user import User  # noqa: F401
from models.exercise import Exercise  # noqa: F401
from models.workout import Workout  # noqa: F401
from models.token import RefreshToken  # noqa: F401


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
