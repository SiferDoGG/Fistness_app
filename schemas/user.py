from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    email: str
    name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
