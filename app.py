import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from graphing.two_week_wait import dataframe_from_criteria
from graphing.plots import activity_by_provider, performance_by_provider

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

    html.Div(children='Gynae Two Week Wait Data (West Midlands)', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='activity-by-provider',
        figure={
            'data': activity_by_provider(df),
            'layout': {
                'title': 'Two Week Wait Activity',
                'yaxis': {
                    'range': [0, 400]
                },
                'font': {
                    'color': colors['graph']
                }
            }
        }
    ),

    dcc.Graph(
        id='performace-by-provider',
        figure={
            'data': performance_by_provider(df),
            'layout': {
                'title': 'Two Week Wait Performance',
                'yaxis': {
                    'range': [0, 100]
                },
                'font': {
                    'color': colors['graph']
                }
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
