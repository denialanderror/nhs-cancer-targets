from typing import List
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


def _total_for_provider(df: pd.DataFrame, provider_code: str) -> go.Scatter:
    grouped = df[df['ODS'] == provider_code].groupby('month_index')
    return go.Scatter(
        x=grouped['month'].sum(),
        y=grouped['total'].sum(),
        mode='lines+markers',
        name=str(grouped['provider'].unique().iloc[0][0] + ' - total referals')
    )


def totals_by_provider(df: pd.DataFrame) -> go.Scatter:
    providers = df['ODS'].unique()
    return [_total_for_provider(df, provider) for provider in providers]
