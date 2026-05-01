"""Промпты для музыкантов."""


def prompt_music_analysis(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    return (
        f"Меня зовут {name}. Мой жанр: {genre}. Платформы: {platforms}.\n\n"
        "На основе моего профиля дай анализ:\n"
        "1. Оценка жанра — насколько конкурентно сейчас?\n"
        "2. Какие платформы приоритетны для этого жанра в 2024-2025\n"
        "3. Три конкретных шага с чего начать продвижение прямо сейчас\n"
        "4. Один совет как выделиться среди похожих артистов"
    )


def prompt_release_plan(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    return (
        f"Артист: {name}. Жанр: {genre}.\n\n"
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
    return (
        f"Артист: {name}. Жанр: {genre}. Платформы: {platforms}.\n\n"
        "Составь контент-план на 7 дней для музыканта.\n"
        "Контент должен строить образ артиста: процесс записи, текст песни, эмоции, история трека.\n"
        "Для каждого дня: платформа, формат (Reels / Stories / пост), идея, хук первых 3 секунд."
    )


def prompt_pitch_label(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    return (
        f"Напиши питч-письмо для лейбла или продюсера от имени артиста {name} ({genre}).\n"
        "Структура: кто я → мой звук → цифры и достижения → что хочу → призыв к действию.\n"
        "Тон: уверенный но не высокомерный. Длина: не больше 200 слов."
    )


def prompt_playlist_pitch(profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    return (
        f"Напиши короткое письмо куратору плейлиста на Spotify или VK Музыке "
        f"от артиста {name} ({genre}).\n"
        "Опиши трек: жанр, настроение, для кого. Объясни почему подходит в их плейлист.\n"
        "Длина: 3-4 предложения максимум."
    )


def prompt_caption_musician(topic: str, profile: dict) -> str:
    name = profile.get("name", "артист")
    genre = ", ".join(profile.get("genre", []))
    return (
        f"Напиши подпись к посту о треке / музыке для артиста {name} ({genre}).\n"
        f"Тема: {topic}\n"
        "Структура: цепляющий хук → 2-3 предложения об эмоции или истории → CTA → 10-15 хэштегов.\n"
        "Тон: живой, артистичный, не рекламный."
    )


def prompt_content_idea_musician(profile: dict) -> str:
    genre = ", ".join(profile.get("genre", []))
    platforms = ", ".join(profile.get("platforms", []))
    return (
        f"Жанр: {genre}. Платформы: {platforms}.\n"
        "Придумай 5 конкретных идей для контента вокруг музыки с вирусным потенциалом.\n"
        "Для каждой: название, хук, почему актуально сейчас, "
        "сложность (легко / средне / сложно)."
    )


def prompt_musician_competitor(artist_name: str, profile: dict) -> str:
    return (
        f"Проанализируй артиста {artist_name}: жанр, как продвигается, "
        "что работает в его контенте, какую аудиторию собирает, "
        "чем наш артист может от него отличиться."
    )
