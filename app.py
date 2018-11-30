import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

df = data.two_week_wait_data()


def providers_by_wait(key):
    grouped = df[['Provider', key]].groupby('Provider')
    return go.Bar(
        x=list(grouped.groups.keys()),
        y=grouped.sum().sort_values(key)[key],
        name=key
    )


app.layout = html.Div([
    dcc.Graph(
        id='Mean wait',
        figure={
            'data': [
                providers_by_wait('Within 14 days'),
                providers_by_wait('15 to 16 days'),
                providers_by_wait('17 to 21 days'),
                providers_by_wait('22 to 28 days'),
                providers_by_wait('After 28 days')
            ],
            'layout': go.Layout(barmode='stack')
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
