from dash import Dash, html, dcc
import plotly.express as px
from data_access import read_gapminder
from plots import plot_scatter

app = Dash(__name__)
gapminder = read_gapminder()
scatter = plot_scatter(gapminder)

app.layout = html.Div(
    children=[
        html.H1("PIB Per cápita vs nacimientos por mujer"),
        dcc.Graph(id="ejercicio1", figure=scatter),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
