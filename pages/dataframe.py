import streamlit as st
from dataset import data_frame

st.title("Dataset de Vendas")
st.dataframe(data_frame)
