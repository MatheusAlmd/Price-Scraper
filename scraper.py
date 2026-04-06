import requests
from bs4 import BeautifulSoup


def buscar_dados(url):
    try:
        # Faz a requisição para a URL que vier da interface
        resposta = requests.get(url)

        # Ajusta os caracteres para não vir símbolo quebrado
        resposta.encoding = "utf-8"

        # Lê o HTML da página
        soup = BeautifulSoup(resposta.text, "html.parser")

        # Pega o título do produto
        titulo_produto = soup.h1.text.strip()

        # Pega o preço, remove o símbolo £ e transforma em número
        preco = float(
            soup.find("p", class_="price_color").text.strip().replace("£", "")
        )

        # Se algum dos dados vier vazio, já interrompe
        if not titulo_produto or not preco:
            print("Título ou preço não foram encontrados corretamente.")
            return None

        # Devolve os dados organizados
        return {
            "titulo_produto": titulo_produto,
            "preco": preco
        }

    except Exception as erro:
        # Se der erro, mostra no terminal e retorna vazio
        print(f"Erro ao buscar dados: {erro}")
        return None