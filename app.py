import dash
from dash import dcc
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Mi Dashboard"),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'},
            ],
            'layout': {
                'title': 'Ejemplo de Gráfico'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
    