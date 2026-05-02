from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_current_user
from app.core.database import get_db
from app.core.limiter import check_limit, increment
from app.models.user import User
from app.schemas.user import SaveProfileRequest

router = APIRouter()


@router.get("")
async def get_profile(current_user: User = Depends(get_current_user)):
    if not current_user.profile:
        return {"completed": False, "user_type": None}
    return {
        "completed": True,
        "user_type": current_user.user_type,
        "profile": current_user.profile,
        "requests_today": current_user.requests_today or 0,
        "plan": current_user.plan,
    }


@router.post("")
async def save_profile(
    body: SaveProfileRequest,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    user_type = body.user_type

    if user_type == "blogger" and not body.niches:
        raise HTTPException(status_code=400, detail="niches обязательны для блогера")
    if user_type == "musician" and not body.genre:
        raise HTTPException(status_code=400, detail="genre обязателен для музыканта")

    if not check_limit(current_user):
        raise HTTPException(
            status_code=429,
            detail=f"Лимит {5} запросов в день исчерпан. Улучши план для безлимитного доступа.",
        )

    profile_data = body.model_dump(exclude={"user_type"}, exclude_none=True)
    current_user.user_type = user_type
    current_user.profile = profile_data

    from app.services.gemini import ask
    if user_type == "blogger":
        from app.services.prompts import prompt_niche_analysis
        ai_prompt = prompt_niche_analysis(profile_data)
    else:
        from app.services.prompts_musician import prompt_music_analysis
        ai_prompt = prompt_music_analysis(profile_data)

    analysis = await ask(ai_prompt, profile_data, user_type)

    increment(current_user)
    await db.commit()
    await db.refresh(current_user)

    return {
        "profile": current_user.profile,
        "user_type": current_user.user_type,
        "analysis": analysis,
    }
