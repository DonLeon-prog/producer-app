"""Промпты для музыкантов."""


def prompt_music_analysis(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    influences = profile.get("influences", "")
    release_status = profile.get("release_status", "")
    goals = profile.get("goals", "")
    influences_line = f"Вдохновляюсь: {influences}.\n" if influences else ""
    status_line = f"Текущий статус: {release_status}.\n" if release_status else ""
    goals_line = f"Моя цель: {goals}.\n" if goals else ""
    return (
        f"Меня зовут {name}. Мой жанр: {genre}. Платформы: {platforms}.\n"
        f"{influences_line}"
        f"{status_line}"
        f"{goals_line}"
        "\nНа основе моего профиля дай анализ:\n"
        "1. Оценка жанра — насколько конкурентно сейчас?\n"
        "2. Какие платформы приоритетны для этого жанра в 2024-2026\n"
        "3. Три конкретных шага с чего начать продвижение прямо сейчас\n"
        "4. Один совет как выделиться среди похожих артистов"
    )


def prompt_release_plan(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    platforms_line = f" Основные платформы: {platforms}." if platforms else ""
    return (
        f"Артист: {name}. Жанр: {genre}.{platforms_line}\n\n"
        "Составь план продвижения трека на 3 недели.\n"
        "Неделя 1 (до релиза): тизеры, behind the scenes, прогрев аудитории.\n"
        "Неделя 2 (релиз): публикации, питч плейлистам, коллаборации.\n"
        "Неделя 3 (после): поддержка трека, сбор обратной связи, следующий шаг.\n"
        "Для каждого дня: платформа, тип контента, конкретная идея поста."
    )


def prompt_content_for_musician(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    influences = profile.get("influences", "")
    influences_line = f" Вдохновляюсь: {influences}." if influences else ""
    return (
        f"Артист: {name}. Жанр: {genre}. Платформы: {platforms}.{influences_line}\n\n"
        "Составь контент-план на 7 дней для музыканта.\n"
        "Контент должен строить образ артиста: процесс записи, текст песни, эмоции, история трека.\n"
        "Для каждого дня: платформа, формат (Reels / Stories / пост), идея, хук первых 3 секунд."
    )


def prompt_pitch_label(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    release_status = profile.get("release_status", "")
    goals = profile.get("goals", "")
    status_line = f" Статус: {release_status}." if release_status else ""
    goals_line = f" Цель: {goals}." if goals else ""
    return (
        f"Напиши питч-письмо для лейбла или продюсера от имени артиста {name} ({genre}).{status_line}{goals_line}\n"
        "Структура: кто я → мой звук → цифры и достижения → что хочу → призыв к действию.\n"
        "Тон: уверенный но не высокомерный. Длина: не больше 200 слов."
    )


def prompt_playlist_pitch(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    platform_line = f" Целевые платформы: {platforms}." if platforms else ""
    return (
        f"Напиши короткое письмо куратору плейлиста от артиста {name} ({genre}).{platform_line}\n"
        "Опиши трек: жанр, настроение, для кого. Объясни почему подходит в их плейлист.\n"
        "Длина: 3-4 предложения максимум."
    )


def prompt_caption_musician(topic: str, profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    platforms_line = f" Платформы: {platforms}." if platforms else ""
    return (
        f"Напиши подпись к посту о треке / музыке для артиста {name} ({genre}).{platforms_line}\n"
        f"Тема: {topic}\n"
        "Структура: цепляющий хук → 2-3 предложения об эмоции или истории → CTA → 10-15 хэштегов.\n"
        "Тон: живой, артистичный, не рекламный."
    )


def prompt_content_idea_musician(profile: dict) -> str:
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    influences = profile.get("influences", "")
    influences_line = f" Вдохновляюсь: {influences}." if influences else ""
    return (
        f"Жанр: {genre}. Платформы: {platforms}.{influences_line}\n"
        "Придумай 5 конкретных идей для контента вокруг музыки с вирусным потенциалом.\n"
        "Для каждой: название, хук, почему актуально сейчас, "
        "сложность (легко / средне / сложно)."
    )


def prompt_musician_competitor(artist_name: str, profile: dict) -> str:
    genre = ", ".join(profile.get("genre", []))
    context = f" Мой жанр: {genre}." if genre else ""
    return (
        f"Проанализируй артиста {artist_name}: жанр, как продвигается, "
        f"что работает в его контенте, какую аудиторию собирает.{context}\n"
        "Чем я могу от него отличиться и привлечь похожую аудиторию?"
    )
