from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, ConfigDict


class ExerciseBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    muscle_group: Optional[str] = None


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseRead(ExerciseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
