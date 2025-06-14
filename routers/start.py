from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboard import get_main_menu, get_info_menu, get_fun_menu



# === Инициализация роутера ===
start_router = Router()

# === Хэндлер на /start ===
@start_router.message(CommandStart())
async def cmd_start(message: Message):
    keyboard = await get_main_menu()
    await message.answer(
        "Привет! Я бот-помощник.\nЧто бы ты хотел сделать дальше?",
        reply_markup = keyboard
    )

# Обработка кнопки "Информация"
@start_router.callback_query(F.data == "info_menu")
async def handle_info(callback: CallbackQuery):
    await callback.message.edit_text(text="Меню информации", reply_markup = await get_info_menu())
    await callback.answer()

# Обработка кнопки "Развлечения"
@start_router.callback_query(F.data == "fun_menu")
async def handle_fun(callback: CallbackQuery):
    await callback.message.delete()
    await callback.message.answer("Меню развлечений", reply_markup=await get_fun_menu())

# Обработка кнопки "Назад"
@start_router.callback_query(F.data == "main_menu")
async def handle_back(callback: CallbackQuery):
    await callback.message.edit_text(text="📋 Главное меню. Выбери действие:", reply_markup = await get_main_menu())
    await callback.answer()

#
# @start_router.callback_query(F.data == "help")
# async def handle_help(callback: CallbackQuery):
#     await callback.message.answer(
#         "📍 Погода — узнай погоду по городу\n"
#         "🌍 Перевод — переведу текст\n"
#         "🖼 Фото — случайное фото\n"
#         "ℹ️ Помощь — показать это меню"
#     )
#     await callback.answer()
#

