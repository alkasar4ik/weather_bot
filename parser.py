import requests


def get_weather(city):
    url = "https://wttr.in/" + city

    response = requests.get(
        url,
        params={
            "format": "j1",
            "lang": "uk"
        },
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    if response.status_code != 200:
        return None

    data = response.json()

    current = data["current_condition"][0]

    return {
        "temperature": current["temp_C"],
        "feels": current["FeelsLikeC"],
        "description": current["weatherDesc"][0]["value"],
        "wind": current["windspeedKmph"],
        "humidity": current["humidity"]
    }