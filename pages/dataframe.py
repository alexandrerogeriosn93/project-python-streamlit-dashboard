import streamlit as st
from dataset import data_frame
from utils import convert_data_to_csv, success_message

st.title("Dataset de Vendas")

with st.expander("Colunas"):
    columns = st.multiselect(
        "Selecione as colunas", list(data_frame.columns), list(data_frame.columns)
    )

st.sidebar.title("Filtros")

with st.sidebar.expander("Categoria do Produto"):
    categories = st.multiselect(
        "Selecione as categorias",
        data_frame["Categoria do Produto"].unique(),
        data_frame["Categoria do Produto"].unique(),
    )

with st.sidebar.expander("Preço do Produto"):
    price = st.slider("Selecione o Preço", 0, 5000, (0, 5000))

with st.sidebar.expander("Data da Compra"):
    date_sale = st.date_input(
        "Selecione a data",
        (data_frame["Data da Compra"].min(), data_frame["Data da Compra"].max()),
    )

query = """
    `Categoria do Produto` in @categories and \
    @price[0] <= `Preço` <= @price[1] and \
    @date_sale[0] <= `Data da Compra` <= @date_sale[1]
"""

filter_data = data_frame.query(query)
filter_data = filter_data[columns]

st.dataframe(filter_data)

st.markdown(
    f"A tabela possui :blue[{filter_data.shape[0]}] linhas e :blue[{filter_data.shape[1]}] colunas"
)
st.markdown("Escreva o nome do arquivo")

first_column, second_column = st.columns(2)

with first_column:
    file_name = st.text_input("", label_visibility="collapsed")
    file_name += ".csv"

with second_column:
    st.download_button(
        "Download do arquivo",
        data=convert_data_to_csv(filter_data),
        file_name=file_name,
        mime="text/csv",
        on_click=success_message,
    )
