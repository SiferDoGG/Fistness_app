from pydantic import BaseModel, ConfigDict


class RefreshTokenBase(BaseModel):
    token: str
    user_id: int


class RefreshTokenCreate(RefreshTokenBase):
    pass


class RefreshTokenRead(RefreshTokenBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshRequest(BaseModel):
    refresh_token: str


class LogoutRequest(BaseModel):
    refresh_token: str


class LoginRequest(BaseModel):
    email: str
    password: str
