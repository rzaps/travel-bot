import requests
from config import UNSPLASH_ACCESS_KEY

def get_random_photo():
    try:
        url = "https://api.unsplash.com/photos/random"
        headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
        response = requests.get(url, headers=headers, timeout=5)
        data = response.json()
        return data.get("urls", {}).get("regular")
    except Exception as e:
        print(f"Ошибка фото: {e}")
        return None