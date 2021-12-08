from dash import dcc,html
from dash.dependencies import Input, Output
from app import app
from layouts import page1, page2
import dash_bootstrap_components as dbc
import callbacks


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}
# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H1("NanoBuild",className="display-5"),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Simple structures", href="/", active="exact"),
                dbc.NavLink("Build from CAD", href="/pages/page1", active="exact"),
                dbc.NavLink("Configuration", href="/pages/page2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar, content
    ])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/pages/page1':
        return page1.layout
    elif pathname == '/pages/page2':
        return page2.layout
    else:
        return page1.layout


if __name__ == '__main__':
    app.run_server(debug=True)
