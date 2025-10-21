# API - Estoques e Produtos

Este projeto é um exemplo prático de CRUD usando:
- Banco de dados  **pgAdmin4**
- Conexão com **psycopg2**
- Interface web com **Streamlit**

## Como executar

### 1. Clonar o repositório
```bash
git clone "https://github.com/Kaylan515/API---Controle-de-Produtos-e-Estoque"
```
### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Configurar variáveis de ambiente
crie um arquivo .env na raiz do projeto com:

DB_NAME=nome_banco

DB_USER=postgres

DB_PASSWORD=sua_senha

DB_HOST=localhost

DB_PORT=5432

### 4. Rodar aplicação
```bash
python -m streamlit run app.py
```
### 4.1 (Recomendação) Utilize o cd no terminal para acessar as pastas back-end e front-end antes de executar os comandos
```bash
python -m uvicorn api:app --reload
```
### Funcionalidades

- Conexão com o banco
- Criar Produtos
- Listar Produtos
- Atualizar preço e estoque
- Deletar Produtos
- Interface simples no streamlit

### Autor
Projeto desenvolvido em aula para treinar API + Banco de Dados

Autor: Kaylan Teodoro