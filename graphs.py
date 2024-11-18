import plotly.express as px
from utils import data_frame_revenue_by_state

graph_map_by_state = px.scatter_geo(
    data_frame_revenue_by_state,
    lat="lat",
    lon="lon",
    scope="south america",
    size="Preço",
    template="seaborn",
    hover_name="Local da compra",
    hover_data={"lat": False, "lon": False},
    title="Receita por Estado",
)
