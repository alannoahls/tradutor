import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import os


def ler_documento(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()


def traduzir_texto(texto, idioma_destino='pt'):
    translator = Translator()
    resultado = translator.translate(texto, dest=idioma_destino)
    return resultado.text


def salvar_documento(caminho_arquivo, conteudo):
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        file.write(conteudo)


def obter_texto_da_url(url):
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se a requisição foi bem-sucedida
        soup = BeautifulSoup(resposta.text, 'html.parser')

        # Tente obter um texto mais específico, como o conteúdo do parágrafo
        paragrafo = soup.find('p')  # Encontra o primeiro parágrafo
        if paragrafo:
            texto = paragrafo.get_text()  # Extrai o texto do parágrafo
            print("Texto extraído da URL:", texto)  # Imprime o texto extraído
            return texto
        else:
            print("Nenhum parágrafo encontrado.")
            return ""
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return ""


# Execução
url = 'https://pt.wikipedia.org/wiki/Ariana_Grande'  # URL escolhida
caminho_saida = 'documento_traduzido.txt'

# Obter texto da URL, traduzir e salvar
texto_url = obter_texto_da_url(url)
if texto_url:  # Verifica se o texto teve sucesso
    texto_traduzido = traduzir_texto(texto_url, 'pt')  # Alvo: português
    print("Texto traduzido:", texto_traduzido)  # Imprime a tradução no terminal
    salvar_documento(caminho_saida, texto_traduzido)
    print("Tradução concluída e salva em:", caminho_saida)
    print("Caminho completo do arquivo:", os.path.abspath(caminho_saida))
else:
    print("Não foi possível obter texto da URL.")
