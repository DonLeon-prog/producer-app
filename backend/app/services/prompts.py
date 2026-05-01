"""Промпты для блогеров."""


def prompt_niche_analysis(profile: dict) -> str:
    name = profile.get("name", "блогер")
    niches = ", ".join(profile.get("niches", []))
    platforms = ", ".join(profile.get("platforms", []))
    return (
        f"Меня зовут {name}. Моя ниша: {niches}. Платформы: {platforms}.\n\n"
        "На основе моего профиля дай анализ:\n"
        "1. Оценка ниши — перегрета или есть место?\n"
        "2. Главные конкуренты и как отличиться\n"
        "3. Три конкретных совета с чего начать прямо сейчас\n"
        "Будь конкретным, без общих слов."
    )


def prompt_week_plan(profile: dict) -> str:
    platforms = ", ".join(profile.get("platforms", ["Instagram Reels"]))
    niches = ", ".join(profile.get("niches", []))
    return (
        f"Составь контент-план на 7 дней для платформы: {platforms}. Ниша: {niches}.\n"
        "Для каждого дня: тема, хук (первые 3 секунды), структура видео, "
        "длина в секундах, лучшее время публикации.\n"
        "Все идеи выполнимы одним человеком без команды."
    )


def prompt_caption(topic: str, profile: dict) -> str:
    return (
        f"Напиши подпись к посту на тему: {topic}\n"
        "Структура: хук → основной текст (2-4 предложения) → CTA → 10-15 хэштегов.\n"
        "Тон: живой, как реальный человек, не копирайтер."
    )


def prompt_video_idea(profile: dict) -> str:
    niches = ", ".join(profile.get("niches", []))
    platforms = ", ".join(profile.get("platforms", []))
    return (
        f"Ниша: {niches}. Платформы: {platforms}.\n"
        "Придумай 5 конкретных идей для видео с вирусным потенциалом.\n"
        "Для каждой: название, хук, почему актуально сейчас, "
        "сложность съёмки (легко / средне / сложно)."
    )


def prompt_competitor(username: str, profile: dict) -> str:
    return (
        f"Проанализируй блогера {username}: ниша, что работает, слабые места, "
        "как выделиться на его фоне."
    )
