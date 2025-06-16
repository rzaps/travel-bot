from aiogram import Router, F
from aiogram.types import CallbackQuery
from db.users import save_user, get_user


# === Инициализация роутера ===
registration_router = Router()

# Обработка кнопки "Регистрация"
@registration_router.callback_query(F.data == "registration")
async def registration(callback: CallbackQuery):
    telegram_id = callback.from_user.id
    name = callback.from_user.full_name
    user = get_user(telegram_id)
    if user:
        await callback.message.answer("Ты уже зарегистрирован!")
    else:
        save_user(telegram_id, name, None)
        await callback.message.answer("Ты зарегистрирован!")
    await callback.answer()