import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# ===== НАСТРОЙКИ =====
BOT_TOKEN = "8043436330:AAGTB1axjNt4zkKABePyo1cKQgpBJH5Klfs"  # Замени на токен от @BotFather
logging.basicConfig(level=logging.INFO)

# ===== ИНИЦИАЛИЗАЦИЯ (исправлено для aiogram 3.7+) =====
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()

# ===== ОБРАБОТЧИКИ КОМАНД =====
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.first_name}!\n"
        "Я базовый бот. Вот мои команды:\n"
        "/help - помощь\n"
        "/info - информация"
    )

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "📌 Доступные команды:\n"
        "/start - приветствие\n"
        "/help - эта справка\n"
        "/info - информация о боте\n\n"
        "📩 Просто напиши любое сообщение — я отвечу эхом."
    )

@dp.message(Command("info"))
async def cmd_info(message: Message):
    await message.answer(
        "🤖 Бот создан на aiogram 3.x\n"
        "📅 Работает 24/7\n"
        "💡 Исходник: 1 файл, ~50 строк"
    )

# ===== ОБРАБОТЧИК ТЕКСТОВЫХ СООБЩЕНИЙ (ЭХО) =====
@dp.message()
async def echo_all(message: Message):
    # Эхо-ответ (можно заменить на свою логику)
    await message.answer(f"📢 Эхо: {message.text}")

# ===== ОБРАБОТКА ОШИБОК =====
@dp.errors()
async def handle_errors(update: types.Update, exception: Exception):
    logging.error(f"Ошибка: {exception}")
    return True  # говорим, что ошибка обработана

# ===== ЗАПУСК =====
async def main():
    print("🚀 Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())