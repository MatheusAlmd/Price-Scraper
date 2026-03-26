import requests
from bs4 import BeautifulSoup


def buscar_dados():
    try:
        # Faz a requisição para a página do produto
        resposta = requests.get("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")

        # Ajusta a codificação para os caracteres virem corretamente
        resposta.encoding = "utf-8"

        # Lê o HTML da página
        soup = BeautifulSoup(resposta.text, "html.parser")

        # Captura o título do produto
        titulo_produto = soup.h1.text.strip()

        # Captura o preço, remove o simbolo e converte para numero
        preco = float(soup.find("p", class_="price_color").text.strip().replace("£", ""))

        # Se algum dado importate vier vazio, interrompe
        if not titulo_produto or not preco:
            print("Título ou preço não foram encontrados corretamente.")
            return None

        # Retorna os dados organizados
        return {
            "titulo_produto": titulo_produto,
            "preco": preco
        }

    except Exception as erro:
        # Mostra o erro caso algo falhe
        print(f"Erro ao buscar dados: {erro}")
        return None