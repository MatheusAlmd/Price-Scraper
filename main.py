from scraper import buscar_dados
from database import criar_banco, salvar_dados, listar_dados
from database import salvar_dados

criar_banco()

dados = buscar_dados()
salvar_dados(dados["titulo_principal"], dados["titulo_pagina"])

print(dados["titulo_principal"])
print(dados["titulo_pagina"])

registros = listar_dados()

for registro in registros:
    print(registro)