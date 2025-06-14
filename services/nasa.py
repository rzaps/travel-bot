import asyncio
import random
import requests
from datetime import datetime, timedelta
from config import NASA_API_KEY


# получить изображение дня
def get_random_apod():
    try:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        random_date = start_date + (end_date - start_date) * random.random()
        date_str = random_date.strftime("%Y-%m-%d")
        url = f"https://api.nasa.gov/planetary/apod?date={date_str}&api_key={NASA_API_KEY}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Проверяем статус ответа
        data = response.json()
        
        # Проверяем наличие необходимых полей
        required_fields = ["url", "title", "explanation"]
        for field in required_fields:
            if field not in data:
                raise KeyError(f"Отсутствует поле {field} в ответе API")
                
        return data
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса к NASA API: {e}")
        raise
    except Exception as e:
        print(f"Неожиданная ошибка при работе с NASA API: {e}")
        raise

