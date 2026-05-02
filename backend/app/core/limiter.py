from datetime import date
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.user import User

FREE_DAILY_LIMIT = 5


def check_limit(user: "User") -> bool:
    """True — запрос разрешён, False — лимит исчерпан."""
    if user.plan in ("pro", "producer"):
        return True
    today = date.today()
    if user.last_request_date != today:
        return True
    return (user.requests_today or 0) < FREE_DAILY_LIMIT


def increment(user: "User") -> None:
    """Увеличивает счётчик запросов. Сбрасывает при смене дня."""
    today = date.today()
    if user.last_request_date != today:
        user.requests_today = 1
        user.last_request_date = today
    else:
        user.requests_today = (user.requests_today or 0) + 1
