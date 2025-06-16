import aiohttp
from config import UNSPLASH_ACCESS_KEY

async def get_random_photo():
    try:
        url = "https://api.unsplash.com/photos/random"
        headers = {"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers, timeout=5) as response:
                data = await response.json()
                return data.get("urls", {}).get("regular")
    except Exception as e:
        print(f"Ошибка фото: {e}")
        return None