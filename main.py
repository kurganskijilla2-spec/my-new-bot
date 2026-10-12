import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from google import genai

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
ai_client = genai.Client(api_key=GEMINI_API_KEY)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот на базе Gemini API. Напиши мне что-нибудь!")

@dp.message()
async def chat_handler(message: types.Message):
    try:
        response = ai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=message.text,
        )
        await message.answer(response.text)
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
