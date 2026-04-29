# Контекст проекта — AI-Продюсер Mini App

## Что мы строим
Telegram Mini App — AI-продюсер для начинающих блогеров.
Пользователь заходит через Telegram, заполняет профиль, получает контент-план,
общается с AI-продюсером в чате. AI работает на Gemini 2.0 Flash (бесплатный).

## Стек
- Frontend: React 18 + TypeScript + Vite + TailwindCSS + Zustand
- Backend: Python FastAPI + PostgreSQL + Redis
- AI: Google Gemini 2.0 Flash API
- Auth: Telegram initData → JWT
- Оплата: Telegram Stars
- Деплой: Railway (бэк) + Vercel (фронт)

## Структура репозитория
- /frontend — React приложение (Telegram Mini App)
- /backend — FastAPI сервер
- /docs — документация
- SPRINTS.md — подробный план по спринтам

## Текущий статус
Спринт 1 — создаём структуру проекта.

## Важные правила
- Весь пользовательский интерфейс на русском языке
- Дизайн: тёмная тема, акцент фиолетовый #7F77DD
- Мобильный first (ширина 390px)
- Все AI ответы через Gemini 2.0 Flash, не через другие модели
- Комментарии в коде на русском языке
