import streamlit as st
from dataset import data_frame
from utils import format_number
from graphs import (
    graph_map_by_state,
    graph_revenue_monthly,
    graph_revenue_state,
    graph_revenue_category,
    graph_revenue_sellers,
    graph_quantity_sales_by_sellers,
)

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas :shopping_trolley:")
st.sidebar.title("Filtro de Vendedores")

filter_seller = st.sidebar.multiselect("Vendedores", data_frame["Vendedor"].unique())

if filter_seller:
    data_frame = data_frame[data_frame["Vendedor"].isin(filter_seller)]

first_tab, second_tab, third_tab = st.tabs(["Dataset", "Receita", "Vendedores"])

with first_tab:
    st.dataframe(data_frame)


with second_tab:
    first_column, second_column = st.columns(2)

    with first_column:
        st.metric("Receita total", format_number(data_frame["Preço"].sum(), "R$"))
        st.plotly_chart(graph_map_by_state, use_container_width=True)
        st.plotly_chart(graph_revenue_state, use_container_width=True)

    with second_column:
        st.metric("Quantidade de vendas", format_number(data_frame.shape[0]))
        st.plotly_chart(graph_revenue_monthly, use_container_width=True)
        st.plotly_chart(graph_revenue_category, use_container_width=True)


with third_tab:
    first_column, second_column = st.columns(2)

    with first_column:
        st.plotly_chart(graph_revenue_sellers)

    with second_column:
        st.plotly_chart(graph_quantity_sales_by_sellers)
