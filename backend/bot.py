import asyncio
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from app.core.config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

_is_https = settings.FRONTEND_URL.startswith("https://")


@dp.message(CommandStart())
async def start(message: Message):
    if _is_https:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(
                text="Открыть AI-Продюсер",
                web_app=WebAppInfo(url=settings.FRONTEND_URL),
            )
        ]])
        await message.answer(
            "Привет! Я твой AI-продюсер 🎬\nНажми кнопку чтобы открыть приложение.",
            reply_markup=keyboard,
        )
    else:
        await message.answer(
            "Привет! Я твой AI-продюсер 🎬\n\n"
            "Приложение пока в разработке — запускается локально.\n"
            f"Когда задеплоишь на Vercel, кнопка появится здесь автоматически."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
