import plotly.express as px
import pandas as pd


def plot_scatter(data: pd.DataFrame):
    return px.scatter(
        data[data.year == 2007],
        x="gdpPercap",
        y="bornPerwom",
        hover_name="country",
    )
