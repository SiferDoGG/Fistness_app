from typing import Dict, List, Optional

from sqlalchemy import JSON, Enum, String
from datetime import UTC, datetime
from sqlalchemy.orm import Mapped, mapped_column

from schemas.enum import WorkoutStatus
from db.base import Base


class Workout(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)

    status: Mapped[WorkoutStatus] = mapped_column(
        Enum(WorkoutStatus), default=WorkoutStatus.scheduled
    )
    notes: Mapped[Optional[str]] = mapped_column(String)

    items: Mapped[Optional[List[Dict]]] = mapped_column(JSON)

    scheduled_at: Mapped[datetime] = mapped_column(nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=lambda: datetime.now(UTC))
    updated_at: Mapped[datetime] = mapped_column(
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
