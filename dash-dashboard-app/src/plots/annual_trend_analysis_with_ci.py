from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

def annual_trend_analysis_with_ci(df, pollutant):
    # Calculate annual mean and confidence intervals
    annual_data = df.groupby(df['date'].dt.year)[pollutant].mean().reset_index()
    annual_data['ci_lower'] = annual_data[pollutant] - 1.96 * (df[pollutant].std() / (df[pollutant].count() ** 0.5))
    annual_data['ci_upper'] = annual_data[pollutant] + 1.96 * (df[pollutant].std() / (df[pollutant].count() ** 0.5))

    # Create the Plotly figure
    fig = go.Figure()

    # Add the mean line
    fig.add_trace(go.Scatter(
        x=annual_data['date'],
        y=annual_data[pollutant],
        mode='lines+markers',
        name='Annual Mean',
        line=dict(color='blue')
    ))

    # Add the confidence interval
    fig.add_trace(go.Scatter(
        x=annual_data['date'],
        y=annual_data['ci_upper'],
        mode='lines',
        name='Upper CI',
        line=dict(color='lightgray'),
        fill='tonexty',
        fillcolor='rgba(0,100,80,0.2)',
        showlegend=False
    ))

    fig.add_trace(go.Scatter(
        x=annual_data['date'],
        y=annual_data['ci_lower'],
        mode='lines',
        name='Lower CI',
        line=dict(color='lightgray'),
        fill='tonexty',
        fillcolor='rgba(0,100,80,0.2)',
        showlegend=False
    ))

    # Update layout
    fig.update_layout(
        title=f'Annual Trend Analysis with CI for {pollutant}',
        xaxis_title='Year',
        yaxis_title=f'{pollutant} Concentration',
        template='plotly_white'
    )

    return fig