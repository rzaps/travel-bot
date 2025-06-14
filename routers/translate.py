from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from services.translate import translate_text

translate_router = Router()

# Кнопка "Перевод" — предлагаем выбрать направление слово
@translate_router.callback_query(F.data == "translate")
async def handle_translate(callback: CallbackQuery):
    await callback.message.answer("Напиши язык и текст. Пример: `/translate en Привет`", parse_mode="Markdown")
    await callback.answer()


# Обработка ввода текста для перевода
@translate_router.message(lambda m: m.text.lower().startswith("/translate"))
async def handle_translate(message: Message):
    parts = message.text.split(maxsplit=2)
    if len(parts) < 3:
        await message.answer("Формат: /translate <язык> <текст>")
        return

    lang = parts[1].lower()
    text = parts[2]

    translated = translate_text(text, lang)
    if translated:
        await message.answer(f"Перевод: {translated}")
    else:
        await message.answer("Произошла ошибка при переводе.")
