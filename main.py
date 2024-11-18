import streamlit as st
import plotly.express as px
from dataset import data_frame

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas :shopping_trolley:")

first_tab, second_tab, third_tab = st.tabs(["Dataset", "Receita", "Vendedores"])

with first_tab:
    st.dataframe(data_frame)
