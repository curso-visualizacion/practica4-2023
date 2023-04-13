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


def get_top5(data: pd.DataFrame, continent: str):
    data.loc[:, "total"] = data.loc[:, range(2005, 2016)].sum(axis=1)
    data_from_continent = data[data.Continent == continent]
    data_ordered = data_from_continent.sort_values(
        "total", ascending=False, inplace=False
    )
    return data_ordered.iloc[:5]


def plot_heatmap(data: pd.DataFrame, continent: str):
    top5 = get_top5(data, continent)
    top5.set_index("Country", inplace=True)
    heatmap = px.imshow(
        top5[range(2005, 2016)],
        labels={"x": "Year", "y": "Country", "color": "Migrantes"},
        x=list(range(2005, 2016)),
        y=top5.index.values,
    )
    return heatmap
