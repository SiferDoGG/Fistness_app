from typing import Optional

from sqlalchemy import String
from datetime import UTC, datetime
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String)

    category: Mapped[Optional[str]] = mapped_column(String)
    muscle_group: Mapped[Optional[str]] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
