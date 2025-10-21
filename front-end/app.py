import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Estoque", page_icon="🏭")
st.title("📦 Estoque de Produtos")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar Produto", "Atualizar Produto", "Deletar"])

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
    st.subheader("🔄 Atualizar produto")

    id_produto = st.number_input("ID do produto a ser atualizado", min_value=1, step=1)
    preco = st.number_input("Novo preço", min_value=0.0, step=0.01)
    quantidade = st.number_input("Nova quantidade", min_value=0, step=1)

    if st.button("Atualizar Produto"):
        if id_produto <= 0:
            st.warning("Informe um ID válido do produto.")
        else:
            dados = {"id_item":id_produto ,"novo_preco": preco, "nova_quantidade": quantidade}
            url = f"{API_URL}/Produtos/{id_produto}"

            st.write(f"📡 URL chamada: {url}")
            response = requests.put(url, params=dados)

            st.write("🔢 Status Code:", response.status_code)
            st.write("📨 Resposta da API:", response.text)

            if response.status_code == 200:
                st.success("✅ Produto atualizado com sucesso!")
            elif response.status_code == 404:
                st.error("❌ Produto não encontrado.")
            else:
                st.error(f"⚠️ Erro ao atualizar o produto. Detalhes: {response.text}")

elif menu == "Deletar":
    st.subheader("🗑️ Excluir produto")

    id_produto = st.number_input("Digite o ID do produto para ser excluído", min_value=1,  step=1)

    if st.button("Excluir Produto"):
        if id_produto > 0:
            dados = {"id_produto": id_produto}
            url = f"{API_URL}/deletar"
            st.write(f"URL chamada: {url}")
            response = requests.delete(url,params=dados)

            st.write("Status Code:", response.status_code)
            st.write("Resposta da API:", response.text)

            if response.status_code == 200:
                st.success("Produto excluído com sucesso!")
            else:
                st.error(f"Erro ao excluir o produto. Detalhes: {response.text}")
        else:
            st.warning("Informe um ID válido do produto.")
  

