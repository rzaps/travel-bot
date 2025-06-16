import asyncio
import random
import aiohttp
from config import CAT_API_KEY

# получить список пород котов
async def get_cat_breeds():
    url = f"https://api.thecatapi.com/v1/breeds"
    headers = {"x-api-key": CAT_API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return await response.json()

# получить фото кота по породе
async def get_cat_image(breed_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}"
    headers = {"x-api-key": CAT_API_KEY}
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            return data[0]["url"]

# # получить информацию о породе
# def get_breed_info(breed_name):
#     breeds = get_cat_breeds()
#     for breed in breeds:
#         if breed["name"].lower() == breed_name.lower():
#             return breed
#     return None

# получить случайную породу
async def get_random_breed():
    breeds = await get_cat_breeds()
    return random.choice(breeds)