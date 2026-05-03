from pydantic import BaseModel
from datetime import datetime


class RefreshTokenBase(BaseModel):
    token: str
    user_id: int


class RefreshTokenCreate(RefreshTokenBase):
    pass


class RefreshTokenRead(RefreshTokenBase):
    id: int

    class Config:
        from_attributes = True
