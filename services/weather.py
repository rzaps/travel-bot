import requests
from config import API_KEY2


def get_weather(city: str):
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY2}&units=metric&lang=ru"
        )
        response = requests.get(url, timeout=15)
        data = response.json()
        print(data)

        if data.get("cod") != 200:
            return None

        return {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
    except Exception as e:
        print(f"Ошибка погоды: {e}")
        return None