import asyncio
import random
import requests
from config import CAT_API_KEY

# получить список пород котов
def get_cat_breeds():
    url = f"https://api.thecatapi.com/v1/breeds"
    headers = {"x-api-key": CAT_API_KEY}
    response = requests.get(url, headers=headers)
    return response.json()

# получить фото кота по породе
def get_cat_image(breed_id):
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}"
    headers = {"x-api-key": CAT_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()
    return data[0]["url"]

# # получить информацию о породе
# def get_breed_info(breed_name):
#     breeds = get_cat_breeds()
#     for breed in breeds:
#         if breed["name"].lower() == breed_name.lower():
#             return breed
#     return None

# получить случайную породу
def get_random_breed():
    breeds = get_cat_breeds()
    return random.choice(breeds)