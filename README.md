# Weather Bot

Telegram-бот для отримання актуальної інформації про погоду в будь-якому місті.

## Features

* Пошук погоди за назвою міста
* Поточна температура
* Відчуття температури
* Стан погоди
* Швидкість вітру
* Вологість
* Простий інтерфейс у Telegram

## Example

```text
🌤 Погода

📍 Фастів
🌡 Температура: 14°C
🤗 Відчувається як: 11°C
☁️ Стан: Overcast
💨 Вітер: 9 км/год
💧 Вологість: 55%
```

## Technologies

* Python
* Aiogram
* HTTPX
* Asyncio
* Weather API

## Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/weather-bot.git
cd weather-bot
```

Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=your_bot_token
WEATHER_API_KEY=your_api_key
```

Run the bot:

```bash
python bot.py
```

## Project Structure

```text
weather-bot/
├── bot.py
├── parser.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Author

**Roma Hom**

Python Developer
