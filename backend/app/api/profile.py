from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any

from app.core.auth import get_current_user
from app.core.database import get_db
from app.models.user import User

router = APIRouter()


@router.get("")
async def get_profile(current_user: User = Depends(get_current_user)):
    """Возвращает профиль пользователя."""
    if not current_user.profile:
        return {"completed": False, "user_type": None}
    return {
        "completed": True,
        "user_type": current_user.user_type,
        "profile": current_user.profile,
    }


@router.post("")
async def save_profile(
    body: dict,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Сохраняет данные онбординга, запускает первичный AI-анализ."""
    user_type = body.get("user_type")
    if user_type not in ("blogger", "musician"):
        raise HTTPException(status_code=400, detail="user_type должен быть 'blogger' или 'musician'")

    current_user.user_type = user_type
    current_user.profile = {k: v for k, v in body.items() if k != "user_type"}

    await db.commit()
    await db.refresh(current_user)

    # AI-анализ после онбординга
    from app.services.gemini import ask
    if user_type == "blogger":
        from app.services.prompts import prompt_niche_analysis
        ai_prompt = prompt_niche_analysis(current_user.profile)
    else:
        from app.services.prompts_musician import prompt_music_analysis
        ai_prompt = prompt_music_analysis(current_user.profile)

    analysis = await ask(ai_prompt, current_user.profile, user_type)

    return {
        "profile": current_user.profile,
        "user_type": current_user.user_type,
        "analysis": analysis,
    }
