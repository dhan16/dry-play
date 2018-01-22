import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def attach_to_app(app: dash.Dash, df: pd.DataFrame):
    cols = df.columns.values

    app.layout = html.Div([
        html.H1('SPE1'),
        html.Div(id='my-div'),
        dcc.Dropdown(
            id='input-column',
            options=[{'label': c, 'value': c} for c in cols],
            value=cols[0]
        ),
        dcc.Input(
            id='input-window',
            placeholder='Enter a window for rolling mean...',
            type='number',
            value=10
        ),
        html.Button('Submit', id='button'),
        dcc.Graph(id='my-graph'),
    ])

    @app.callback(
        Output('my-graph', 'figure'),
        [Input('button', 'n_clicks')],
        [State('input-column', 'value'), State('input-window', 'value')]
    )
    def update_graph(n_clicks, column, window):
        mdf = df.rolling(window).mean()
        return {
            'data': [
                {
                    'x': df.index,
                    'y': df[column],
                    'name': column,
                },
                {
                    'x': mdf.index,
                    'y': mdf[column],
                    'name': 'avg({0}, {1})'.format(column, window)

                },
            ]
        }