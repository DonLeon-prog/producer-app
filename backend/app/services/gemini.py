from google import genai
from google.genai import types
from typing import AsyncGenerator

from app.core.config import settings

SYSTEM_BLOGGER = (
    "Ты — AI-продюсер для начинающих блогеров (Instagram Reels, TikTok, YouTube Shorts). "
    "Думай как опытный продюсер с 10 годами в digital. Знаешь алгоритмы 2024-2026, "
    "что цепляет в первые 3 секунды, как строить личный бренд с нуля. "
    "Говори как умный друг — конкретно, без воды. Всегда на русском."
)

SYSTEM_MUSICIAN = (
    "Ты — AI-продюсер для начинающих музыкантов и певцов. "
    "Знаешь как продвигать треки на Spotify, VK Музыке, YouTube, как питчить лейблам, "
    "как строить аудиторию вокруг музыки через короткий контент. "
    "Знаешь что работает в 2024-2026: Reels с отрывком трека, behind the scenes записи, "
    "stories с текстами песен. Говори как умный друг — конкретно, без воды. Всегда на русском."
)

_client = genai.Client(api_key=settings.GEMINI_API_KEY)
_MODEL = "gemini-2.5-flash"


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


async def ask(prompt: str, profile: dict, user_type: str) -> str:
    context = build_profile_context(profile, user_type)
    full_prompt = f"{context}\n\n{prompt}" if context else prompt
    response = await _client.aio.models.generate_content(
        model=_MODEL,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            system_instruction=get_system_prompt(user_type),
        ),
    )
    return response.text


async def stream(prompt: str, profile: dict, user_type: str) -> AsyncGenerator[str, None]:
    context = build_profile_context(profile, user_type)
    full_prompt = f"{context}\n\n{prompt}" if context else prompt
    async for chunk in await _client.aio.models.generate_content_stream(
        model=_MODEL,
        contents=full_prompt,
        config=types.GenerateContentConfig(
            system_instruction=get_system_prompt(user_type),
        ),
    ):
        if chunk.text:
            yield chunk.text
