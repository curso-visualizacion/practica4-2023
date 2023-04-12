from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

gapminder = pd.read_csv("dashboard/static/gapminderData2.csv")

scatter = px.scatter(
    gapminder[gapminder.year == 2007],
    x="gdpPercap",
    y="bornPerwom",
    hover_name="country",
)

app.layout = html.Div(
    children=[
        html.H1("PIB Per cápita vs nacimientos por mujer"),
        dcc.Graph(id="ejercicio1", figure=scatter),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
