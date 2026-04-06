import streamlit as st
from scraper import buscar_dados
from database import criar_banco, salvar_dados, listar_dados

# título da página
st.title("Monitor de Preços")

# texto curto explicando a ideia da interface
st.write("Escolha um dos produtos abaixo para consultar o preço.")

# garante que o banco exista antes de usar
criar_banco()

# lista com 3 produtos fixos para a demo
produtos_predefinidos = [
    {
        "Produto": "A Light in the Attic",
        "URL": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    },
    {
        "Produto": "Tipping the Velvet",
        "URL": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
    },
    {
        "Produto": "Soumission",
        "URL": "https://books.toscrape.com/catalogue/soumission_998/index.html"
    }
]

# mostra a tabelinha com os produtos disponíveis
st.subheader("Produtos disponíveis para consulta")
st.dataframe(produtos_predefinidos, use_container_width=True, hide_index=True)

# cria uma lista só com os nomes para o usuário escolher
nomes_produtos = [produto["Produto"] for produto in produtos_predefinidos]

# caixa de seleção do produto
produto_escolhido = st.selectbox("Escolha um produto:", nomes_produtos)

# pega a URL do produto escolhido
url_produto = next(
    produto["URL"] for produto in produtos_predefinidos
    if produto["Produto"] == produto_escolhido
)

# quando clicar, busca o preço do produto escolhido
if st.button("Buscar preço"):
    dados = buscar_dados(url_produto)

    # se encontrar os dados, salva no banco e mostra na tela
    if dados:
        salvar_dados(dados["titulo_produto"], dados["preco"])

        st.subheader("Resultado da busca")
        st.write(f"**Título:** {dados['titulo_produto']}")
        st.write(f"**Preço atual:** {dados['preco']}")
    else:
        st.error("Não foi possível buscar os dados do produto.")

# busca todo o histórico já salvo
registros = listar_dados()

# se existir histórico, mostra em tabela
if registros:
    st.subheader("Histórico de consultas")

    tabela_historico = []
    for registro in registros:
        tabela_historico.append({
            "ID": registro[0],
            "Título do produto": registro[1],
            "Preço": registro[2],
            "Data da coleta": registro[3]
        })

    st.dataframe(tabela_historico, use_container_width=True, hide_index=True)