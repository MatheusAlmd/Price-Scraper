import sqlite3
from datetime import datetime


def criar_banco():
    conexao = sqlite3.connect("monitor_precos.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS historico_precos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo_produto TEXT,
        preco TEXT,
        data_coleta TEXT
    )
""")

    conexao.commit()
    conexao.close()


def salvar_dados(titulo_produto, preco):
    conexao = sqlite3.connect("monitor_precos.db")
    cursor = conexao.cursor()
    data_coleta = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO historico_precos (titulo_produto, preco, data_coleta)
    VALUES (?, ?, ?)
""", (titulo_produto, preco, data_coleta))

    conexao.commit()
    conexao.close()

def listar_dados():
    conexao = sqlite3.connect("monitor_precos.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM historico_precos")
    registros = cursor.fetchall()

    conexao.close()
    return registros