import json
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import get_current_user
from app.core.database import get_db
from app.core.limiter import check_limit, increment
from app.models.user import User
from app.schemas.ai import ChatRequest, CaptionRequest, AnalyzeRequest, PitchRequest

router = APIRouter()


async def require_limit(current_user: User):
    """Проверяет лимит и выбрасывает 429 если исчерпан."""
    allowed = await check_limit(str(current_user.id), current_user.plan)
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="Дневной лимит запросов исчерпан. Улучши план для безлимитного доступа.",
        )
    await increment(str(current_user.id))


@router.post("/plan")
async def get_plan(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """Контент-план на 7 дней."""
    await require_limit(current_user)
    from app.services.gemini import ask

    if current_user.user_type == "blogger":
        from app.services.prompts import prompt_week_plan
        prompt = prompt_week_plan(current_user.profile or {})
    else:
        from app.services.prompts_musician import prompt_content_for_musician
        prompt = prompt_content_for_musician(current_user.profile or {})

    result = await ask(prompt, current_user.profile or {}, current_user.user_type)
    return {"plan": result, "cached": False}


@router.post("/chat")
async def chat_stream(
    body: ChatRequest,
    current_user: User = Depends(get_current_user),
):
    """AI-чат со стримингом через Server-Sent Events."""
    await require_limit(current_user)
    from app.services.gemini import stream

    async def event_generator():
        async for chunk in stream(body.message, current_user.profile or {}, current_user.user_type):
            yield f"data: {json.dumps({'text': chunk})}\n\n"
        yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")


@router.post("/caption")
async def get_caption(
    body: CaptionRequest,
    current_user: User = Depends(get_current_user),
):
    """Подпись к посту."""
    await require_limit(current_user)
    from app.services.gemini import ask

    if current_user.user_type == "blogger":
        from app.services.prompts import prompt_caption
        prompt = prompt_caption(body.topic, current_user.profile or {})
    else:
        from app.services.prompts_musician import prompt_caption_musician
        prompt = prompt_caption_musician(body.topic, current_user.profile or {})

    result = await ask(prompt, current_user.profile or {}, current_user.user_type)
    return {"result": result}


@router.post("/idea")
async def get_idea(
    current_user: User = Depends(get_current_user),
):
    """5 идей для контента."""
    await require_limit(current_user)
    from app.services.gemini import ask

    if current_user.user_type == "blogger":
        from app.services.prompts import prompt_video_idea
        prompt = prompt_video_idea(current_user.profile or {})
    else:
        from app.services.prompts_musician import prompt_content_idea_musician
        prompt = prompt_content_idea_musician(current_user.profile or {})

    result = await ask(prompt, current_user.profile or {}, current_user.user_type)
    return {"result": result}


@router.post("/analyze")
async def analyze(
    body: AnalyzeRequest,
    current_user: User = Depends(get_current_user),
):
    """Анализ конкурента / похожего артиста."""
    await require_limit(current_user)
    from app.services.gemini import ask

    if current_user.user_type == "blogger":
        from app.services.prompts import prompt_competitor
        prompt = prompt_competitor(body.username or "", current_user.profile or {})
    else:
        from app.services.prompts_musician import prompt_musician_competitor
        prompt = prompt_musician_competitor(body.artist or "", current_user.profile or {})

    result = await ask(prompt, current_user.profile or {}, current_user.user_type)
    return {"result": result}


@router.post("/release-plan")
async def release_plan(
    current_user: User = Depends(get_current_user),
):
    """План продвижения трека на 3 недели (только для музыкантов)."""
    if current_user.user_type != "musician":
        raise HTTPException(status_code=403, detail="Только для музыкантов")
    await require_limit(current_user)
    from app.services.gemini import ask
    from app.services.prompts_musician import prompt_release_plan

    result = await ask(prompt_release_plan(current_user.profile or {}), current_user.profile or {}, "musician")
    return {"result": result}


@router.post("/pitch")
async def pitch(
    body: PitchRequest,
    current_user: User = Depends(get_current_user),
):
    """Питч для лейбла или куратора плейлиста (только для музыкантов)."""
    if current_user.user_type != "musician":
        raise HTTPException(status_code=403, detail="Только для музыкантов")
    if body.type not in ("label", "playlist"):
        raise HTTPException(status_code=400, detail="type должен быть 'label' или 'playlist'")

    await require_limit(current_user)
    from app.services.gemini import ask

    if body.type == "label":
        from app.services.prompts_musician import prompt_pitch_label
        prompt = prompt_pitch_label(current_user.profile or {})
    else:
        from app.services.prompts_musician import prompt_playlist_pitch
        prompt = prompt_playlist_pitch(current_user.profile or {})

    result = await ask(prompt, current_user.profile or {}, "musician")
    return {"result": result}
