from scraper import buscar_dados
from database import criar_banco, salvar_dados, listar_dados


criar_banco()

dados = buscar_dados()
salvar_dados(dados["titulo_produto"], dados["preco"])

print(dados["titulo_produto"])
print(dados["preco"])

registros = listar_dados()

for registro in registros:
    print(f"ID: {registro[0]}")
    print(f"Título do produto: {registro[1]}")
    print(f"Preço: {registro[2]}")
    print(f"Data da coleta: {registro[3]}")
    print("-" * 30)