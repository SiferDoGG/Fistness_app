from pydantic import BaseModel, ConfigDict

class RefreshTokenBase(BaseModel):
    token: str
    user_id: int


class RefreshTokenCreate(RefreshTokenBase):
    pass


class RefreshTokenRead(RefreshTokenBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
