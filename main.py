from scraper import buscar_dados
from database import criar_banco, salvar_dados, listar_dados

# Cria o banco de dados e a tabela, caso ainda não existam
criar_banco()

# Busca os dados da página
dados = buscar_dados()

# Se houver erro no Scraper o programa encerra aqui.
if dados is None:
    print("Falha ao buscar dados.")
    exit()

# Salva no banco o título do produto e o preço 
salvar_dados(dados["titulo_produto"], dados["preco"])

# Mostra no terminal os dados coletados
print(dados["titulo_produto"])
print(dados["preco"])

# Busca todos os registros salvos no banco
registros = listar_dados()

# Mostra cada registro de maneira organizada no terminal!
for registro in registros:
    print(f"ID: {registro[0]}")
    print(f"Título do produto: {registro[1]}")
    print(f"Preço: {registro[2]}")
    print(f"Data da coleta: {registro[3]}")
    print("-" * 30)