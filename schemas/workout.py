from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, ConfigDict

from schemas.enum import WorkoutStatus


class WorkoutBase(BaseModel):
    title: str
    status: WorkoutStatus = WorkoutStatus.scheduled
    notes: Optional[str] = None
    items: Optional[List[Dict]] = None
    scheduled_at: datetime


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutRead(WorkoutBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
