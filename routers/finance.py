from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.inline_keyboard import get_main_menu, finance_keyboard
from db.users import update_finance, get_finance_data


# === Инициализация роутера ===
finance_router = Router()

# Обработка кнопки "Финансы"
class FinanceForm(StatesGroup):
    category1 = State()
    expenses1 = State()
    category2 = State()
    expenses2 = State()
    category3 = State()
    expenses3 = State()

# Обработка кнопки "Финансы"
@finance_router.callback_query(F.data == "finance")
async def start_finance(callback: CallbackQuery, state: FSMContext):
    print(f"DEBUG: Кнопка 'Финансы' нажата пользователем {callback.from_user.id}")
    await state.set_state(FinanceForm.category1)
    await callback.message.answer("Введите первую категорию расходов:")
    await callback.answer()

# Обработка кнопки "Показать статистику"
@finance_router.callback_query(F.data == "show_finance")
async def show_finance_stats(callback: CallbackQuery):
    tg_id = callback.from_user.id
    finance_data = get_finance_data(tg_id)
    
    if finance_data:
        # Формируем красивый отчет
        report = f"💰 <b>Ваши расходы:</b>\n\n"
        report += f"📊 <b>Общая сумма:</b> {finance_data['total']:,.2f} ₽\n\n"
        
        for category, amount, percentage in finance_data['breakdown']:
            # Создаем визуальный индикатор процента
            bar_length = int(percentage / 5)  # 5% = 1 символ
            bar = "█" * bar_length + "░" * (20 - bar_length)
            
            report += f"📌 <b>{category}:</b>\n"
            report += f"   💵 {amount:,.2f} ₽ ({percentage:.1f}%)\n"
            report += f"   {bar}\n\n"
        
        await callback.message.answer(report, parse_mode="HTML", reply_markup=finance_keyboard())
    else:
        await callback.message.answer("📝 У вас пока нет данных о расходах. Нажмите '💰 Финансы' для добавления.", reply_markup=finance_keyboard())
    
    await callback.answer()

# Обработка кнопки "Назад" в финансах
@finance_router.callback_query(F.data == "main_menu")
async def back_to_main_menu(callback: CallbackQuery):
    await callback.message.edit_text(
        text="📋 Главное меню. Выбери действие:",
        reply_markup=await get_main_menu()
    )
    await callback.answer()

# Обработка ввода первой категории
@finance_router.message(FinanceForm.category1)
async def category1_handler(message: Message, state: FSMContext):
    await state.update_data(category1=message.text)
    await state.set_state(FinanceForm.expenses1)
    await message.answer("Введите расходы для категории 1:")

# Обработка ввода расходов
@finance_router.message(FinanceForm.expenses1)
async def expenses1_handler(message: Message, state: FSMContext):
    try:
        expense = float(message.text)
        await state.update_data(expenses1=expense)
        await state.set_state(FinanceForm.category2)
        await message.answer("Введите вторую категорию расходов:")
    except ValueError:
        await message.answer("❌ Пожалуйста, введите корректную сумму (например: 1000.50)")

# Обработка ввода второй категории
@finance_router.message(FinanceForm.category2)
async def category2_handler(message: Message, state: FSMContext):
    await state.update_data(category2=message.text)
    await state.set_state(FinanceForm.expenses2)
    await message.answer("Введите расходы для категории 2:")

# Обработка ввода расходов
@finance_router.message(FinanceForm.expenses2)
async def expenses2_handler(message: Message, state: FSMContext):
    try:
        expense = float(message.text)
        await state.update_data(expenses2=expense)
        await state.set_state(FinanceForm.category3)
        await message.answer("Введите третью категорию расходов:")
    except ValueError:
        await message.answer("❌ Пожалуйста, введите корректную сумму (например: 1000.50)")

# Обработка ввода третьей категории
@finance_router.message(FinanceForm.category3)
async def category3_handler(message: Message, state: FSMContext):
    await state.update_data(category3=message.text)
    await state.set_state(FinanceForm.expenses3)
    await message.answer("Введите расходы для категории 3:")

# Обработка ввода расходов
@finance_router.message(FinanceForm.expenses3)
async def expenses3_handler(message: Message, state: FSMContext):
    try:
        expense = float(message.text)
        await state.update_data(expenses3=expense)
        data = await state.get_data()
        tg_id = message.from_user.id
        
        # Сохраняем данные
        update_finance(tg_id, data)
        
        # Получаем статистику
        finance_data = get_finance_data(tg_id)
        
        if finance_data:
            # Формируем красивый отчет
            report = f"💰 <b>Ваши расходы:</b>\n\n"
            report += f"📊 <b>Общая сумма:</b> {finance_data['total']:,.2f} ₽\n\n"
            
            for category, amount, percentage in finance_data['breakdown']:
                # Создаем визуальный индикатор процента
                bar_length = int(percentage / 5)  # 5% = 1 символ
                bar = "█" * bar_length + "░" * (20 - bar_length)
                
                report += f"📌 <b>{category}:</b>\n"
                report += f"   💵 {amount:,.2f} ₽ ({percentage:.1f}%)\n"
                report += f"   {bar}\n\n"
            
            await message.answer(report, parse_mode="HTML")
        else:
            await message.answer("✅ Данные сохранены!")
            
        await state.clear()
        
    except ValueError:
        await message.answer("❌ Пожалуйста, введите корректную сумму (например: 1000.50)")