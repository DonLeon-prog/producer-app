"""Промпты для блогеров."""


def prompt_niche_analysis(profile: dict) -> str:
    name = profile.get("name", "блогер")
    niches = ", ".join(profile.get("niches", []))
    platforms = ", ".join(profile.get("platforms", []))
    inspiration = profile.get("inspiration", "")
    goals = profile.get("goals", "")
    inspiration_line = f"Вдохновляюсь: {inspiration}.\n" if inspiration else ""
    goals_line = f"Моя цель: {goals}.\n" if goals else ""
    return (
        f"Меня зовут {name}. Ниша: {niches}. Платформы: {platforms}.\n"
        f"{inspiration_line}"
        f"{goals_line}"
        "\nНа основе моего профиля дай анализ:\n"
        "1. Оценка ниши — перегрета или есть место?\n"
        "2. Главные конкуренты и как отличиться\n"
        "3. Три конкретных совета с чего начать прямо сейчас\n"
        "Будь конкретным, без общих слов."
    )


def prompt_week_plan(profile: dict) -> str:
    platforms = ", ".join(profile.get("platforms", ["Instagram Reels"]))
    niches = ", ".join(profile.get("niches", []))
    inspiration = profile.get("inspiration", "")
    inspiration_line = f" Вдохновляюсь стилем: {inspiration}." if inspiration else ""
    return (
        f"Составь контент-план на 7 дней для платформы: {platforms}. Ниша: {niches}.{inspiration_line}\n"
        "Для каждого дня: тема, хук (первые 3 секунды), структура видео, "
        "длина в секундах, лучшее время публикации.\n"
        "Все идеи выполнимы одним человеком без команды."
    )


def prompt_caption(topic: str, profile: dict) -> str:
    platforms = ", ".join(profile.get("platforms", []))
    niches = ", ".join(profile.get("niches", []))
    context = f" Платформы: {platforms}. Ниша: {niches}." if platforms or niches else ""
    return (
        f"Напиши подпись к посту на тему: {topic}.{context}\n"
        "Структура: хук → основной текст (2-4 предложения) → CTA → 10-15 хэштегов.\n"
        "Тон: живой, как реальный человек, не копирайтер."
    )


def prompt_video_idea(profile: dict) -> str:
    niches = ", ".join(profile.get("niches", []))
    platforms = ", ".join(profile.get("platforms", []))
    inspiration = profile.get("inspiration", "")
    inspiration_line = f" Вдохновляюсь: {inspiration}." if inspiration else ""
    return (
        f"Ниша: {niches}. Платформы: {platforms}.{inspiration_line}\n"
        "Придумай 5 конкретных идей для видео с вирусным потенциалом.\n"
        "Для каждой: название, хук, почему актуально сейчас, "
        "сложность съёмки (легко / средне / сложно)."
    )


def prompt_competitor(username: str, profile: dict) -> str:
    niches = ", ".join(profile.get("niches", []))
    context = f" Моя ниша: {niches}." if niches else ""
    return (
        f"Проанализируй блогера {username}: ниша, что работает, слабые места.{context}\n"
        "Как мне выделиться на его фоне и привлечь часть его аудитории?"
    )
