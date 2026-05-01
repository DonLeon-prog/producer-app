from typing import Optional, Any
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

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    access_token: str
    user: UserResponse
