from typing import List
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


def _activity_for_provider(df: pd.DataFrame, provider_code: str) -> go.Scatter:
    grouped = df[df['ODS'] == provider_code].groupby('month_index')
    return go.Scatter(
        x=grouped['month'].sum(),
        y=grouped['total'].sum(),
        mode='lines+markers',
        name=str(grouped['provider'].unique().iloc[0][0] + ' - total referals')
    )


def activity_by_provider(df: pd.DataFrame) -> List[go.Scatter]:
    providers = df['ODS'].unique()
    return [_activity_for_provider(df, provider) for provider in providers]


def _performance_for_provider(df: pd.DataFrame, provider_code: str) -> go.Scatter:
    grouped = df[df['ODS'] == provider_code].groupby('month_index')
    return go.Scatter(
        x=grouped['month'].sum(),
        y=grouped['percentage'].sum(),
        mode='lines+markers',
        name=str(grouped['provider'].unique().iloc[0][0]
                 + ' - percentage target reached')
    )


def performance_by_provider(df: pd.DataFrame) -> List[go.Scatter]:
    providers = df['ODS'].unique()
    return [_performance_for_provider(df, provider) for provider in providers]
