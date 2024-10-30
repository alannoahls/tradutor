from googletrans import Translator
from config import API_KEY, API_ENDPOINT

def traduzir_texto(texto, idioma_destino="en"):
    translator = Translator()
    traducao = translator.translate(texto, dest=idioma_destino)
    return traducao.text

from googletrans import Translator

def traduzir_texto(texto, idioma_destino="en"):
    try:
        translator = Translator()
        traducao = translator.translate(texto, dest=idioma_destino)
        return traducao.text
    except Exception as e:
        return f"Erro ao traduzir: {e}"
