import requests
from bs4 import BeautifulSoup

def buscar_dados():
    resposta = requests.get("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")
    resposta.encoding = "utf-8"
    soup = BeautifulSoup(resposta.text, "html.parser")
    

    titulo_produto = soup.h1.text.strip()
    preco = soup.find("p", class_="price_color").text.strip().replace("£", "")
    

    return {
        "titulo_produto": titulo_produto,
        "preco": preco
    }
