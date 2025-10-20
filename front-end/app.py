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

elif menu == "Atualizar Produto":
    st.subheader("✏️ Atualizar produto")

    id_produto = st.number_input("ID do produto", step=1, min_value=1)
    novo_preco = st.number_input("Novo preço", step=0.5)
    nova_quantidade = st.number_input("Nova quantidade", step=1)

    if st.button("Atualizar Produto"):
        if not id_produto:
            st.warning("Informe o ID do produto para atualizar.")
        else:
            params = {"novo_preco": novo_preco, "nova_quantidade": nova_quantidade}
            response = requests.put(f"{API_URL}/Produtos/{id_produto}", params=params)

            if response.status_code == 200:
                st.success("✅ Produto atualizado com sucesso!")
            elif response.status_code == 404:
                st.error("❌ Produto não encontrado.")
            else:
                st.error("⚠️ Erro ao atualizar o produto.")
