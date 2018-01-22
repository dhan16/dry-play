import dash
import dash_html_components as html
from dash.dependencies import Output, Input, State

from poc.ui.dynamic_controls import DynamicControls

app = dash.Dash()
app.config.supress_callback_exceptions = True

dyn1 = DynamicControls(app, 'dyn1')
dyn2 = DynamicControls(app, 'dyn2', childtypes=['button', 'textinput'])
app.layout = html.Div([
    dyn1.component(),
    dyn2.component(),
    html.Button('Go', id='go'),
    html.Div(id='output')
])
dyn1.init_callbacks()
dyn2.init_callbacks()

@app.callback(
    Output('output', 'children'),
    [Input('go', 'n_clicks')],
    [State(dyn1.divid, 'children'), State(dyn2.divid, 'children')])
def go(n_clicks, dyn1_children, dyn2_children):
    print(dyn1_children)
    print(dyn2_children)
    return 'Grrrr {0}'.format(n_clicks)


if __name__ == '__main__':
    app.run_server(debug=True)
