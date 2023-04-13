from dash import Dash, html, dcc
from data_access import read_gapminder, read_migrantes
from plots import plot_heatmap, plot_scatter
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
gapminder = read_gapminder()
migrantes = read_migrantes()
scatter = plot_scatter(gapminder)
heatmap = plot_heatmap(migrantes)

app.layout = dbc.Container(
    fluid=True,
    children=[
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H1("PIB Per cápita vs nacimientos por mujer"),
                        dcc.Graph(id="ejercicio1", figure=scatter),
                    ],
                    width=7,
                ),
                dbc.Col(
                    [
                        html.H1("Heatmap Migrantes por Año"),
                        dcc.Graph(id="heatmap", figure=heatmap),
                    ]
                ),
            ]
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
