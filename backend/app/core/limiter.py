from datetime import date
# import redis.asyncio as aioredis  # Redis отключён, добавим позже
# from .config import settings

FREE_DAILY_LIMIT = 5

# _redis: aioredis.Redis | None = None


# def get_redis() -> aioredis.Redis:
#     global _redis
#     if _redis is None:
#         _redis = aioredis.from_url(settings.REDIS_URL, decode_responses=True)
#     return _redis


async def check_limit(user_id: str, plan: str) -> bool:
    """Возвращает True если запрос разрешён, False если лимит исчерпан."""
    if plan in ("pro", "producer"):
        return True
    # TODO: подключить Redis счётчик
    return True


async def increment(user_id: str) -> None:
    """Увеличивает счётчик запросов."""
    # TODO: подключить Redis счётчик
    pass


def _end_of_day_timestamp() -> int:
    from datetime import datetime
    tomorrow = datetime.combine(date.today(), datetime.min.time()).replace(hour=23, minute=59, second=59)
    return int(tomorrow.timestamp())
