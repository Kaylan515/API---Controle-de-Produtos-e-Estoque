from fastapi import FastAPI
from funcao import listar_produtos, deletar_produtos, criar_tabela, inserir_produto, atualizar_produto, buscar_estoque

# Rodar o fastapi:
# python -m uvicorn api:app --reload

# /docs > Documentação Swagger
# /redoc > Documentação redoc

app = FastAPI(title="Estoque de produtos")

#GET = Pegar / listar
#POST = Criar / Enviar
#PUT = Atualizar
#DELETE = deletar

# 127.0.0.1:8000
@app.get("/")
def home():
    return{"mensagem": "Bem-vindo ao Estoque de produtos"}

@app.post("/Produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    inserir_produto(nome, categoria, preco, quantidade)
    return { "mensagem": "Produto adicionado com sucesso!"}
