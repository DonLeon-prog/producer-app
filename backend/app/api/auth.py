from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.auth import validate_telegram_init_data, create_jwt_token
from app.core.config import settings
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import TelegramAuthRequest, AuthResponse, UserResponse

router = APIRouter()


@router.post("/telegram", response_model=AuthResponse)
async def telegram_auth(body: TelegramAuthRequest, db: AsyncSession = Depends(get_db)):
    """Авторизация через Telegram initData."""
    tg_user = validate_telegram_init_data(body.init_data, settings.BOT_TOKEN)

    telegram_id = str(tg_user["id"])
    result = await db.execute(select(User).where(User.telegram_id == telegram_id))
    user = result.scalar_one_or_none()

    if not user:
        user = User(
            telegram_id=telegram_id,
            username=tg_user.get("username"),
            first_name=tg_user.get("first_name"),
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)

    token = create_jwt_token(str(user.id))
    return AuthResponse(
        access_token=token,
        user=UserResponse(
            id=str(user.id),
            telegram_id=user.telegram_id,
            username=user.username,
            first_name=user.first_name,
            user_type=user.user_type,
            profile=user.profile,
            plan=user.plan,
        ),
    )
