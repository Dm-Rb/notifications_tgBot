import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from config_file import Config


# Инициализация бота
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: Message):
    """Команда /start возвращает пользователю его chat_id(user_id)"""

    await message.answer(f"Ваш chat_id:\n{message.chat.id}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())