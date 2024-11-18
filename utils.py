from dataset import data_frame


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
