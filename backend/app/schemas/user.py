from typing import Optional, Any, Literal
from pydantic import BaseModel


class TelegramAuthRequest(BaseModel):
    init_data: str


class UserResponse(BaseModel):
    id: str
    telegram_id: str
    username: Optional[str] = None
    first_name: Optional[str] = None
    user_type: Optional[str] = None
    profile: Optional[Any] = None
    plan: str = "free"
    requests_today: int = 0

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    access_token: str
    user: UserResponse


class SaveProfileRequest(BaseModel):
    user_type: Literal["blogger", "musician"]
    name: str
    platforms: list[str]
    goals: Optional[str] = None
    # blogger
    niches: Optional[list[str]] = None
    inspiration: Optional[str] = None
    # musician
    genre: Optional[list[str]] = None
    influences: Optional[str] = None
    release_status: Optional[str] = None
