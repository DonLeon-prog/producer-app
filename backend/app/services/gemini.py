import google.generativeai as genai
from typing import AsyncGenerator

from app.core.config import settings

SYSTEM_BLOGGER = (
    "Ты — AI-продюсер для начинающих блогеров (Instagram Reels, TikTok, YouTube Shorts). "
    "Думай как опытный продюсер с 10 годами в digital. Знаешь алгоритмы 2024-2025, "
    "что цепляет в первые 3 секунды, как строить личный бренд с нуля. "
    "Говори как умный друг — конкретно, без воды. Всегда на русском."
)

SYSTEM_MUSICIAN = (
    "Ты — AI-продюсер для начинающих музыкантов и певцов. "
    "Знаешь как продвигать треки на Spotify, VK Музыке, YouTube, как питчить лейблам, "
    "как строить аудиторию вокруг музыки через короткий контент. "
    "Знаешь что работает в 2024-2025: Reels с отрывком трека, behind the scenes записи, "
    "stories с текстами песен. Говори как умный друг — конкретно, без воды. Всегда на русском."
)


def get_system_prompt(user_type: str) -> str:
    return SYSTEM_MUSICIAN if user_type == "musician" else SYSTEM_BLOGGER


def build_profile_context(profile: dict, user_type: str) -> str:
    if not profile:
        return ""
    if user_type == "blogger":
        return (
            f"Профиль блогера: имя — {profile.get('name', '?')}, "
            f"ниша — {', '.join(profile.get('niches', []))}, "
            f"платформы — {', '.join(profile.get('platforms', []))}, "
            f"вдохновение — {profile.get('inspiration', '?')}, "
            f"цель — {profile.get('goals', '?')}."
        )
    return (
        f"Профиль музыканта: имя — {profile.get('name', '?')}, "
        f"жанр — {', '.join(profile.get('genre', []))}, "
        f"платформы — {', '.join(profile.get('platforms', []))}, "
        f"вдохновение — {profile.get('influences', '?')}, "
        f"статус — {profile.get('release_status', '?')}, "
        f"цель — {profile.get('goals', '?')}."
    )


def _get_model(user_type: str):
    genai.configure(api_key=settings.GEMINI_API_KEY)
    return genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction=get_system_prompt(user_type),
    )


async def ask(prompt: str, profile: dict, user_type: str) -> str:
    """Одиночный запрос к Gemini, возвращает строку."""
    context = build_profile_context(profile, user_type)
    full_prompt = f"{context}\n\n{prompt}" if context else prompt

    model = _get_model(user_type)
    response = await model.generate_content_async(full_prompt)
    return response.text


async def stream(prompt: str, profile: dict, user_type: str) -> AsyncGenerator[str, None]:
    """Стриминг ответа от Gemini по чанкам."""
    context = build_profile_context(profile, user_type)
    full_prompt = f"{context}\n\n{prompt}" if context else prompt

    model = _get_model(user_type)
    async for chunk in await model.generate_content_async(full_prompt, stream=True):
        if chunk.text:
            yield chunk.text
