import streamlit as st
import plotly.express as px
from dataset import data_frame

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas :shopping_trolley:")

first_tab, second_tab, third_tab = st.tabs(["Dataset", "Receita", "Vendedores"])

with first_tab:
    st.dataframe(data_frame)


with second_tab:
    first_column, second_column = st.columns(2)

    with first_column:
        st.metric("Receita total", data_frame["Preço"].sum())

    with second_column:
        st.metric("Quantidade de vendas", data_frame.shape[0])
