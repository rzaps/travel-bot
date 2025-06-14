from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from services.photo import get_random_photo
from keyboards.inline_keyboard import photo_again_keyboard

photo_router = Router()

# Обработка кнопки "photo"
@photo_router.callback_query(F.data == "photo")
async def handle_photo(callback: CallbackQuery):
    url = get_random_photo()
    if url:
        await callback.message.delete()
        await callback.message.answer_photo(photo=url, caption="Вот случайное фото", reply_markup = photo_again_keyboard())
    else:
        await callback.message.answer("Не удалось получить фото.")
    await callback.answer()

# Обработка кнопки "photo_again"
@photo_router.callback_query(F.data == "photo_again")
async def photo_again(callback: CallbackQuery):
    url = get_random_photo()
    if url:
        await callback.message.answer_photo(photo=url, caption="Ещё одно фото", reply_markup = photo_again_keyboard())
    else:
        await callback.message.answer("Не удалось получить фото.")
    await callback.answer()
