import requests
from bs4 import BeautifulSoup

def buscar_dados():
    resposta = requests.get("https://cursos.alura.com.br/dashboard")
    soup = BeautifulSoup(resposta.text, "html.parser")

    titulo_principal = soup.h1.text.strip()
    titulo_pagina = soup.title.text.strip()

    return {
        "titulo_principal": titulo_principal,
        "titulo_pagina": titulo_pagina
    }
