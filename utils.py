from dataset import data_frame
import pandas as pd
import streamlit as st
import time


def format_number(value, prefix=""):
    for unit in ["", "mil"]:
        if value < 1000:
            return f"{prefix} {value:.2f} {unit}"

        value /= 1000

    return f"{prefix} {value:.2f} milhões"


data_frame_revenue_by_state = data_frame.groupby("Local da compra")[["Preço"]].sum()
data_frame_revenue_by_state = (
    data_frame.drop_duplicates(subset="Local da compra")[
        ["Local da compra", "lat", "lon"]
    ]
    .merge(data_frame_revenue_by_state, left_on="Local da compra", right_index=True)
    .sort_values("Preço", ascending=False)
)

data_frame_revenue_monthly = (
    data_frame.set_index("Data da Compra")
    .groupby(pd.Grouper(freq="ME"))["Preço"]
    .sum()
    .reset_index()
)
data_frame_revenue_monthly["Ano"] = data_frame_revenue_monthly["Data da Compra"].dt.year
data_frame_revenue_monthly["Mes"] = data_frame_revenue_monthly[
    "Data da Compra"
].dt.month_name()

data_frame_revenue_by_category = (
    data_frame.groupby("Categoria do Produto")[["Preço"]]
    .sum()
    .sort_values("Preço", ascending=False)
)

data_frame_sellers = pd.DataFrame(
    data_frame.groupby("Vendedor")["Preço"].agg(["sum", "count"])
)


@st.cache_data
def convert_data_to_csv(data):
    return data.to_csv(index=False).encode("utf-8")


def success_message():
    success = st.success("Download do arquivo concluído com sucesso.", icon="✅")
    time.sleep(3)
    success.empty()
