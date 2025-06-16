from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder



# Главное меню
async def get_main_menu():
    keyboard_main =InlineKeyboardBuilder()
    keyboard_main.add(
        InlineKeyboardButton(text="🧭 Информация", callback_data="info_menu"),
                InlineKeyboardButton(text="🎉 Развлечения", callback_data="fun_menu"),
                InlineKeyboardButton(text="👤 Регистрация", callback_data="registration"),
                InlineKeyboardButton(text="❓ Что я умею", callback_data="help")
    )
    return keyboard_main.adjust(2).as_markup()

# Подменю "Информация для путешествия"
async def get_info_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
                #InlineKeyboardButton(text="📍 Где я?", callback_data="location"),
                InlineKeyboardButton(text="☁️ Погода", callback_data="weather"),
                InlineKeyboardButton(text="🌐 Перевод", callback_data="translate"),
                InlineKeyboardButton(text="💱 Валюта", callback_data="currency"),
                InlineKeyboardButton(text="💰 Финансы", callback_data="finance"),
                InlineKeyboardButton(text="📊 Статистика расходов", callback_data="show_finance"),
                InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
                 )
    return keyboard.adjust(2).as_markup()

# Подменю "Развлечения в дороге"
async def get_fun_menu():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🖼️ Фото", callback_data="photo"),
                InlineKeyboardButton(text="🚀 Космос", callback_data="space"),
                InlineKeyboardButton(text="🐱 Коты", callback_data="cat"),
                InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
                )
    return keyboard.adjust(2).as_markup()

# Кнопка "Ещё фото"
def photo_again_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🖼️ Ещё фото", callback_data="photo_again"),
                InlineKeyboardButton(text="🔙 Назад", callback_data="fun_menu")
                )
    return keyboard.adjust(2).as_markup()

# Кнопка "Ещё фото из космоса"
def nasa_again_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🖼️ Ещё фото из космоса", callback_data="nasa_again"),
                InlineKeyboardButton(text="🔙 Назад", callback_data="fun_menu")
                )
    return keyboard.adjust(2).as_markup()

# Кнопка "Ещё кота"
def cat_again_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="🐾 Ещё кота", callback_data="cat_again"),
        InlineKeyboardButton(text="🔙 Назад", callback_data="fun_menu")
    )
    return keyboard.adjust(2).as_markup()

# Кнопка "Обновить погоду"
def weather_refresh_keyboard(city: str):
     keyboard = InlineKeyboardBuilder()
     keyboard.add(
        InlineKeyboardButton(text="🔄 Обновить погоду", callback_data=f"refresh_weather:{city}"),
        InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
     )
     return keyboard.adjust(2).as_markup()

# Кнопки для финансов
def finance_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="📊 Показать статистику", callback_data="show_finance"),
        InlineKeyboardButton(text="🔙 Назад", callback_data="main_menu")
    )
    return keyboard.adjust(2).as_markup()
