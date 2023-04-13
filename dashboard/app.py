from dash import Dash, Input, Output, html, dcc
from data_access import read_gapminder, read_migrantes
from plots import plot_heatmap, plot_scatter
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
gapminder = read_gapminder()
migrantes = read_migrantes()
scatter = plot_scatter(gapminder)
heatmap = plot_heatmap(migrantes, "América")

continent_options = [
    {"label": continent, "value": continent}
    for continent in migrantes.Continent.unique()
]

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
                        dbc.Select(
                            id="select-continentes",
                            options=continent_options,
                            value="América",
                        ),
                        dcc.Graph(id="heatmap", figure=heatmap),
                    ]
                ),
            ]
        ),
    ],
)


@app.callback(
    Output(component_id="heatmap", component_property="figure"),
    Input(component_id="select-continentes", component_property="value"),
)
def update_heatmap(continent):
    return plot_heatmap(migrantes, continent)


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
