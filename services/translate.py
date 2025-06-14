from deep_translator import GoogleTranslator

def translate_text(text: str, target_lang: str = "en") -> str:
    try:
        return GoogleTranslator(source="auto", target=target_lang).translate(text)
    except Exception as e:
        print(f"Ошибка перевода: {e}")
        return ""