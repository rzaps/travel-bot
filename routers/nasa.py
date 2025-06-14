from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from services.nasa import get_random_apod
from keyboards.inline_keyboard import nasa_again_keyboard

nasa_router = Router()


@nasa_router.callback_query(F.data == "space")
async def handle_space(callback: CallbackQuery):
    try:
        apod = get_random_apod()
        photo_url = apod["url"]
        title = apod["title"]
        explanation = apod["explanation"]
        await callback.message.answer_photo(photo=photo_url, caption=f"{title}\n\n{explanation}", reply_markup=nasa_again_keyboard())
    except Exception as e:
        await callback.message.answer("Извините, не удалось получить фото из космоса. Попробуйте позже.")
        print(f"Ошибка NASA API: {e}")
    await callback.answer()


@nasa_router.callback_query(F.data == "nasa_again")
async def handle_nasa_again(callback: CallbackQuery):
    try:
        apod = get_random_apod()
        photo_url = apod["url"]
        title = apod["title"]
        explanation = apod["explanation"]
        await callback.message.answer_photo(photo=photo_url, caption=f"{title}\n\n{explanation}", reply_markup=nasa_again_keyboard())
    except Exception as e:
        await callback.message.answer("Извините, не удалось получить фото из космоса. Попробуйте позже.")
        print(f"Ошибка NASA API: {e}")
    await callback.answer()
