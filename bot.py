
import asyncio
import json
import os

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from parser import get_weather


load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


cities = [
    "Вишневе",
    "Київ",
    "Львів",
    "Біла Церква",
    "Одеса",
    "Харків",
    "Дніпро",
    "Вінниця",
    "Черкаси",
    "Запоріжжя",

    "Ужгород",
    "Івано-Франківськ",
    "Тернопіль",
    "Хмельницький",
    "Чернівці",
    "Рівне",
    "Луцьк",
    "Житомир",
    "Полтава",
    "Суми",
    "Кропивницький",
    "Миколаїв",
    "Херсон",
    "Кривий Ріг",
    "Маріуполь",
    "Кременчук",
    "Бровари",
    "Ірпінь",
    "Буча",
    "Обухів",
    "Фастів",
    "Бердичів",
    "Кам'янець-Подільський",
    "Мукачево",
    "Дрогобич",
    "Стрий",
    "Нікополь",
    "Павлоград",
    "Краматорськ",
    "Слов'янськ",
    "Бахмут",
    "Мелітополь",
    "Бердянськ",
    "Умань",
    "Прилуки",
    "Ніжин",
    "Коростень",
    "Чортків",
    "Бориспіль"
]

def load_users():
    if not os.path.exists("users.json"):
        return {}

    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


def create_keyboard(user_id):
    users = load_users()

    user_id = str(user_id)

    favorites = users.get(user_id, [])

    result = []

    for city in favorites:
        if city not in result:
            result.append(city)

    for city in cities:
        if city not in result:
            result.append(city)

    keyboard = InlineKeyboardBuilder()

    for city in result:
        if city in favorites:
            text = "⭐ " + city
        else:
            text = "🇺🇦 " + city

        keyboard.button(
            text=text,
            callback_data="city:" + city
        )

    keyboard.adjust(2)

    return keyboard.as_markup()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌤 Привіт!\n\n"
        "Натисни /weather, щоб вибрати місто."
    )


@dp.message(Command("weather"))
async def weather_menu(message: Message):
    keyboard = create_keyboard(message.from_user.id)

    await message.answer(
        "🌤 Обери місто:",
        reply_markup=keyboard
    )


@dp.callback_query(lambda callback: callback.data.startswith("city:"))
async def city_weather(callback: CallbackQuery):
    city = callback.data.replace("city:", "")

    weather_data = get_weather(city)

    if weather_data is None:
        await callback.message.answer(
            "❌ Не вдалося отримати погоду."
        )
        await callback.answer()
        return

    users = load_users()

    user_id = str(callback.from_user.id)

    if user_id not in users:
        users[user_id] = []

    if city in users[user_id]:
        users[user_id].remove(city)

    users[user_id].insert(0, city)

    save_users(users)

    text = (
        "🌤 Погода\n\n"
        f"📍 {city}\n"
        f"🌡 Температура: {weather_data['temperature']}°C\n"
        f"🤗 Відчувається як: {weather_data['feels']}°C\n"
        f"☁️ Стан: {weather_data['description']}\n"
        f"💨 Вітер: {weather_data['wind']} км/год\n"
        f"💧 Вологість: {weather_data['humidity']}%"
    )

    await callback.message.answer(text)

    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

