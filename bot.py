import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from parser import get_weather


TOKEN = "8940609597:AAHkTM3trqRwVuO-3TiFEvOd0t2wlFKqJO8"


bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌤 Привіт!\n\n"
        "Напиши місто:\n"
        "/weather Вишневе\n"
        "/weather Київ\n"
        "/weather Львів"
    )


@dp.message(Command("weather"))
async def weather(message: Message):
    parts = message.text.split(maxsplit=1)

    if len(parts) < 2:
        await message.answer(
            "❌ Напиши місто.\n\n"
            "Наприклад:\n"
            "/weather Вишневе"
        )
        return

    city = parts[1]

    try:
        weather_data = get_weather(city)
    except Exception:
        weather_data = None

    if weather_data is None:
        await message.answer(
            "❌ Не вдалося знайти це місто."
        )
        return

    text = (
        "🌤 Погода\n\n"
        f"📍 {city}\n"
        f"🌡 Температура: {weather_data['temperature']}°C\n"
        f"🤗 Відчувається як: {weather_data['feels']}°C\n"
        f"☁️ Стан: {weather_data['description']}\n"
        f"💨 Вітер: {weather_data['wind']} км/год\n"
        f"💧 Вологість: {weather_data['humidity']}%"
    )

    await message.answer(text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())