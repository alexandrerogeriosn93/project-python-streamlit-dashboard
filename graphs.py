import plotly.express as px
from utils import data_frame_revenue_by_state, data_frame_revenue_monthly

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

graph_revenue_monthly = px.line(
    data_frame_revenue_monthly,
    x="Mes",
    y="Preço",
    markers=True,
    range_y=(0, data_frame_revenue_monthly.max()),
    color="Ano",
    line_dash="Ano",
    title="Receita Mensal",
)

graph_revenue_monthly.update_layout(yaxis_title="Receita")

graph_revenue_state = px.bar(
    data_frame_revenue_by_state.head(5),
    x="Local da compra",
    y="Preço",
    text_auto=True,
    title="Maior Receita por Estados",
)
