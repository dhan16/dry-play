import dash
import os
import pandas as pd

from poc.funcs.columnstats import attach_to_app

datadir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
    'resources',
    'poc')
file = os.path.join(datadir, 'data.csv')

df = pd.DataFrame.from_csv(file)
app = dash.Dash()
attach_to_app(app, df)
if __name__ == '__main__':
    app.run_server()
