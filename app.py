import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from graphing.two_week_wait import dataframe_from_criteria
from graphing.plots import totals_by_provider

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = dataframe_from_criteria()

colors = {
    'background': '#0269c0',
    'graph': '#037dd4',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='NHS Cancer Statistics',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Activity per Provider (West Midlands)', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='activity-by-provider',
        figure={
            'data': totals_by_provider(df),
            'layout': {
                # 'plot_bgcolor': colors['graph'],
                # 'paper_bgcolor': colors['graph'],
                'font': {
                    'color': colors['graph']
                }
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
