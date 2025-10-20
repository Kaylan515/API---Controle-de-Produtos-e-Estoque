import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Estoque", page_icon="🏭")
st.title("📦 Estoque de Produtos")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar Produto", "Atualizar Produto"])

if menu == "Catalogo":
    st.subheader("Todos os produtos disponiveis")
    response = requests.get(f"{API_URL}/Produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
    else:
        st.error("Erro ao acessar a API")

elif menu == "Adicionar Produto":
    st.subheader("➕ Adicionar produto")
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("categoria")
    preco = st.number_input("Preço do produto", step=0.5)
    quantidade = st.number_input("quantidade do produto", step=1)
    if st.button("Adicionar Produto"):
        dados = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        response = requests.post(f"{API_URL}/Produtos", params=dados)
        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar o Produto")
