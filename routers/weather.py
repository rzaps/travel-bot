from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from services.weather import get_weather
from keyboards.inline_keyboard import weather_refresh_keyboard, get_main_menu
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from db.users import save_user

# === Состояние формы пользователя ===
class UserForm(StatesGroup):
    city = State()

weather_router = Router()

# Обработка кнопки "Погода" — спрашиваем город
@weather_router.callback_query(F.data == "weather")
async def ask_city(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("В каком городе ты хочешь узнать погоду?")
    await state.set_state(UserForm.city)
    await callback.answer()

# Обработка ввода города
@weather_router.message(UserForm.city)
async def process_city(message: Message, state: FSMContext):
    city = message.text
    user_id = message.from_user.id
    name = message.from_user.full_name

    # Сохраняем данные в БД
    save_user(user_id, name, city)

    await message.answer(f"✅ Город <b>{city}</b> сохранён!", parse_mode="HTML")

    # Показываем погоду сразу после сохранения
    await send_weather(message, city)

    # Сбрасываем состояние
    await state.clear()

# Обработка кнопки "refresh_weather"
@weather_router.callback_query(F.data.startswith("refresh_weather:"))
async def refresh_weather(callback: CallbackQuery):
    city = callback.data.split(":")[1]
    await send_weather(callback.message, city)
    await callback.answer()

# Обработка кнопки "Назад"
@weather_router.callback_query(F.data == "main_menu")
async def back_to_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="📋 Главное меню. Выбери действие:",
        reply_markup=await get_main_menu()
    )
    await callback.answer()

# Функция для отправки погоды
async def send_weather(target, city: str):
    data = await get_weather(city)
    if not data:
        await target.answer(
            f"Не удалось получить погоду для {city}",
            reply_markup=weather_refresh_keyboard(city)
        )
        return
    temp = data['temp']
    desc = data['description'].capitalize()
    await target.answer(
        f"🌤 Погода в {city}: {temp}°C, {desc}",
        reply_markup=weather_refresh_keyboard(city)
    )