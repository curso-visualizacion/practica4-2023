from dash import Dash, html

app = Dash(__name__)
server = app.server

app.layout = html.Div(children="Hello World")


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0", port="5000")
