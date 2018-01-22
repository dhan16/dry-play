from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html


class BaseDynamicControls:
    def __init__(self, app, divid, childtypes = None):
        self.app = app
        self.divid = divid
        self.childtypes = childtypes
        self.add_button_id = divid + '_add_button'
        self.childtype_selector_id = divid + '_childtype_selector'
        self.childcount = 0
        children = [html.Button('Add', id=self.add_button_id)]
        if childtypes is not None:
            children.insert(0, html.Div(children=[dcc.Dropdown(id=self.childtype_selector_id,
                                            options= [{'label': t, 'value': t} for t in childtypes])]))
        self.div = html.Div(children=[
            html.Div(id=self.divid),
            html.Div(children=children)
        ])

    def create_child(self, childid, childtype):
        raise Exception('Unimplemented')

    def component(self):
        return self.div

    def init_callbacks(self):
        app = self.app
        self.__init_remover_callbacks()
        def add_child(n_clicks, childtype, current_val):
            if n_clicks is None:
                return current_val
            self.childcount = self.childcount + 1
            childid = self.__childid(self.childcount)
            child = self.create_child(childid + '_Real', childtype)
            current_children = [] if current_val is None else current_val['props']['children']
            return html.Div(current_children + [html.Div(id=childid, children=[
                child,
                self.__get_remover(childid)
            ])])
        if self.childtypes is None:
            @app.callback(
                Output(self.divid, 'children'),
                [Input(self.add_button_id, 'n_clicks')],
                [State(self.divid, 'children')])
            def add_button(n_clicks, current_val):
                return add_child(n_clicks, None, current_val)
        else:
            @app.callback(
                Output(self.divid, 'children'),
                [Input(self.add_button_id, 'n_clicks')],
                [State(self.childtype_selector_id, 'value'), State(self.divid, 'children')])
            def add_button(n_clicks, childtype, current_val):
                return add_child(n_clicks, childtype, current_val)

    def __childid(self, i):
        return '{0}_Child{1}'.format(self.divid, i)

    def __create_remover(self, childid):
        app = self.app
        removerid = childid + 'remover'
        div = html.Button("X", id=removerid)
        app.callback(
            Output(childid, 'children'),
            [Input(removerid, 'n_clicks')],
            [State(childid, 'children')])(
            self.__generate_remover_callback(childid)
        )
        return div

    def __generate_remover_callback(self, childid):
        def remove_callback(n_clicks, current_val):
            print('Removing ' + childid)
            if n_clicks is None:
                return current_val
            return None
        return remove_callback

    def __init_remover_callbacks(self):
        """Plotly being a pain we have to register all callbacks before the application runs!"""
        self.removers = {}
        for i in range(1, 100):
            childid = self.__childid(i)
            self.removers[childid] = self.__create_remover(childid)

    def __get_remover(self, childid):
        return self.removers[childid]


class DynamicControls(BaseDynamicControls):
    def create_child(self, childid, childtype):
        if childtype == 'textinput':
            return dcc.Input(
                id=childid,
                type='text',
            )
        else:
            return html.Button("Button"+childid, id=childid)
