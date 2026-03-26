import sqlite3
from datetime import datetime


def criar_banco():
    # Abre a conexão com o banco
    conexao = sqlite3.connect("monitor_precos.db")
    cursor = conexao.cursor()

    # Cria a tabela se ela ainda não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS historico_precos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_produto TEXT,
            preco REAL,
            data_coleta TEXT
        )
    """)

    # Salva a criação da tabela no banco
    conexao.commit()

    # Fecha a conexão
    conexao.close()


def salvar_dados(titulo_produto, preco):
    # Abre a conexão com o banco
    conexao = sqlite3.connect("monitor_precos.db")
    cursor = conexao.cursor()

    # Pega a data e hora exata da coleta
    data_coleta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Insere os dados do produto na tabela
    cursor.execute("""
        INSERT INTO historico_precos (titulo_produto, preco, data_coleta)
        VALUES (?, ?, ?)
    """, (titulo_produto, preco, data_coleta))

    # Salva os dados no banco
    conexao.commit()

    # Fecha a conexão
    conexao.close()


def listar_dados():
    # Abre a conexão com o banco
    conexao = sqlite3.connect("monitor_precos.db")
    cursor = conexao.cursor()

    # Busca todos os registros salvos
    cursor.execute("SELECT * FROM historico_precos")
    registros = cursor.fetchall()

    # Fecha a conexão
    conexao.close()

    # Retorna a lista com os registros encontrados
    return registros