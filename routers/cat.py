# from aiogram import Router, F
# from aiogram.filters import Command
# from aiogram.types import Message, CallbackQuery
# from services.cat import get_breed_info, get_cat_image
#
# cat_router = Router()
#
# @cat_router.callback_query(F.data == "cat")
# async def handle_cat(callback: CallbackQuery):
#     await callback.message.answer("Напиши породу кота:")
#     await callback.answer()
#
# @cat_router.message(F.text.regexp(r"^[^/].*"))
# async def cat_breed(message: Message):
#     breed_name = message.text
#     breed_info = get_breed_info(breed_name)
#     if breed_info:
#         cat_image = get_cat_image(breed_info["id"])
#         info = (f"Порода: {breed_info['name']}\n"
#                 f"Описание: {breed_info['description']}\n"
#                 f"Темперамент: {breed_info['temperament']}\n"
#                 f"Страна: {breed_info['origin']}\n"
#                 f"Ссылка: {breed_info['wikipedia_url']}")
#         await message.answer_photo(photo=cat_image, caption=info)
#     else:
#         await message.answer("Порода не найдена.")


from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline_keyboard import cat_again_keyboard
from services.cat import get_random_breed, get_cat_image

cat_router = Router()

@cat_router.callback_query(F.data == "cat")
async def handle_cat(callback: CallbackQuery):
    breed_info = await get_random_breed()
    if breed_info:
        cat_image = await get_cat_image(breed_info["id"])
        info = (
            f"🐱 Порода: {breed_info['name']}\n"
            f"📄 Описание: {breed_info['description']}\n"
            f"🎭 Темперамент: {breed_info['temperament']}\n"
            f"🌍 Страна: {breed_info['origin']}\n"
            f"🔗 Подробнее: {breed_info['wikipedia_url']}"
        )
        await callback.message.delete()
        await callback.message.answer_photo(photo=cat_image, caption=info, reply_markup=cat_again_keyboard())
    else:
        await callback.message.answer("❌ Не удалось получить породу.")
    await callback.answer()


@cat_router.callback_query(F.data == "cat_again")
async def cat_again(callback: CallbackQuery):
    breed_info = await get_random_breed()
    if breed_info:
        cat_image = await get_cat_image(breed_info["id"])
        info = (
            f"🐱 Порода: {breed_info['name']}\n"
            f"📄 Описание: {breed_info['description']}\n"
            f"🎭 Темперамент: {breed_info['temperament']}\n"
            f"🌍 Страна: {breed_info['origin']}\n"
            f"🔗 Подробнее: {breed_info['wikipedia_url']}"
        )
        await callback.message.answer_photo(photo=cat_image, caption=info, reply_markup=cat_again_keyboard())
    else:
        await callback.message.answer("❌ Не удалось получить породу.")
    await callback.answer()
