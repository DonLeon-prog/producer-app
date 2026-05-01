import httpx
from app.core.config import settings


async def send_notification(telegram_id: str, text: str) -> None:
    """Отправляет сообщение пользователю через Bot API."""
    url = f"https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"chat_id": telegram_id, "text": text, "parse_mode": "HTML"})
