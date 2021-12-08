import dash
import dash_bootstrap_components as dbc
external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css",
    "https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.0/font/bootstrap-icons.css"
]
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=external_stylesheets)
app.title = 'Nanobuild'
server = app.server


