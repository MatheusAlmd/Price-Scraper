# Monitor de Preços

Projeto simples em Python para pegar o título e o preço de um produto em uma página web e salvar esse histórico em um banco SQLite.

## O que esse projeto faz

- acessa uma página de produto
- coleta o nome do produto
- coleta o preço atual
- salva os dados em banco
- registra a data da coleta
- mostra o histórico no terminal

## Tecnologias

- Python
- requests
- BeautifulSoup
- SQLite

## Arquivos principais

- `main.py` -> roda o fluxo principal
- `scraper.py` -> faz a coleta dos dados da página
- `database.py` -> cria o banco, salva e lista os registros

## Como rodar

1. Criar o ambiente virtual, ativar, instalar as dependências e rodar o projeto:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python main.py

```

### Exemplo do que é salvo
 - Título do produto
 - Preço
 - Data e hora da coleta


 ### O que eu pratiquei aqui
 - Requisições HTTP
 - Scraping com BeautifulSoup
 - Manipulação de HTML
 - Uso de SQlite com Python
 - Separação do projeto em arquivos
 - Tratamento básico de erro


 ### Melhorias Futuras
 - Permitir trocar URL sem editar o código
 - Monitorar mais de um produto
 - Criar alerta de queda de preço
 - Melhorar a exibição de registros


 

 ### Observação 
 Esse projeto foi feito para estudo e para portfólio, usando uma página simples de teste para praticar scraping.


### Autor: Matheus Almeida