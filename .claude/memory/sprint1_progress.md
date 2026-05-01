---
name: Спринт 1 — прогресс и решённые проблемы
description: Что сделано в Спринте 1, какие проблемы решили, текущее состояние проекта
type: project
---

## Выполнено сегодня (2026-05-01)

### Задача 1.3 — Структура бэкенда
Создана вся файловая структура `backend/app/`:
- `core/` — config.py, database.py, auth.py, limiter.py
- `models/` — user.py
- `schemas/` — user.py, ai.py
- `api/` — auth.py, profile.py, ai.py, billing.py
- `services/` — gemini.py, prompts.py, prompts_musician.py, telegram.py
- `app/main.py` — FastAPI + CORS + роутеры + GET /health
- `backend/.env.example`

### Задача 1.4 — База данных (Alembic + Neon)
- Alembic инициализирован, `env.py` переписан под async engine
- `alembic/env.py` читает `DATABASE_URL` из `settings` (не из alembic.ini)
- SSL для asyncpg передаётся через `connect_args={"ssl": ssl.create_default_context()}`
- Миграция `55e549d320a8_create_users_table` — таблица `users` создана в Neon
- Колонка `plan` — `String` + CHECK constraint (не native enum, чтобы избежать конфликтов)
- БД: Neon PostgreSQL (cloud), не локальный Docker

### Задача 1.5 — Docker
- Создан `docker-compose.yml` в корне (postgres:16 + redis:7)
- Для текущей разработки Docker не используется — подключены к Neon напрямую

### Задача 1.7 — Telegram Bot
- `backend/bot.py` — aiogram 3, polling
- На localhost показывает текстовое сообщение (Telegram не принимает http:// для WebApp)
- WebApp кнопка появится автоматически когда `FRONTEND_URL` станет https://

---

## Текущее состояние

### .env (backend/.env)
- `DATABASE_URL` — Neon PostgreSQL (asyncpg, без `?sslmode=require` в URL — SSL через connect_args)
- `REDIS_URL` — закомментирован, Redis отключён
- `BOT_TOKEN` — реальный токен бота установлен
- `GEMINI_API_KEY` — заглушка (нужно получить на aistudio.google.com)
- `JWT_SECRET` — локальная заглушка (нужно поменять для продакшена)

### Что НЕ сделано из Спринта 1
- Задача 1.6 — автодеплой (GitHub Actions, Railway, Vercel) — пропущена
- Frontend структура пока не тронута (только базовый Vite из задачи 1.2)

### Следующий шаг
Спринт 2 — авторизация и онбординг:
- 2.1 Авторизация через Telegram initData
- 2.2 Подключение Gemini (нужен GEMINI_API_KEY)
- 2.3–2.4 Промпты (уже написаны в services/)
- 2.5 API профиля
- 2.6–2.9 Фронт: онбординг блогера и музыканта

---

## Важные решения

**Why:** Neon вместо локального Docker — проще для начала, не нужен Docker Desktop.
**How to apply:** DATABASE_URL всегда указывает на Neon. Для prod Railway создаст свою БД.

**Why:** `plan` как String вместо native PostgreSQL enum — SQLAlchemy дублировал CREATE TYPE даже с `create_type=False`, ломая миграцию.
**How to apply:** В моделях и миграциях всегда String + CHECK constraint для plan.

**Why:** SSL через `connect_args={"ssl": ssl_ctx}`, а не `?sslmode=require` в URL — asyncpg не понимает `sslmode` параметр в connection string.
**How to apply:** Так в `database.py` и в `alembic/env.py`.

**Why:** Redis отключён — пока не нужен, лимиты временно не работают (check_limit всегда True).
**How to apply:** Когда подключим Redis, раскомментировать `limiter.py` и `REDIS_URL` в `.env`.
