from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from services.currency import get_currency


# === Инициализация роутера ===
currency_router = Router()

# Обработка кнопки "currency"
@currency_router.callback_query(F.data == "currency")
async def handle_currency(callback: CallbackQuery):
    try:
        currency_data = await get_currency()
        await callback.message.answer(currency_data)
    except Exception as e:
        await callback.message.answer("Произошла ошибка при получении курса валют")
        print(f"Ошибка при получении курса валют: {e}")
    await callback.answer()