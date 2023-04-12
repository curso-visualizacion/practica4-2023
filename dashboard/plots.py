import plotly.express as px
import pandas as pd


def plot_scatter(data: pd.DataFrame):
    return px.scatter(
        data,
        x="gdpPercap",
        y="bornPerwom",
        size="pop",
        color="continent",
        hover_name="country",
        size_max=50,
        animation_frame="year",
        range_y=[0, 9],
        range_x=[-1000, 60000],
    )
