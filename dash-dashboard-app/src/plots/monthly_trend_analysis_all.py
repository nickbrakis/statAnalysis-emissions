from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd

def monthly_trend_analysis_all(df, pollutant):
    # Grouping the data by month and year
    df['YearMonth'] = df['date'].dt.to_period('M')
    monthly_data = df.groupby('YearMonth')[pollutant].mean().reset_index()

    # Creating the Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly_data['YearMonth'].astype(str), 
                               y=monthly_data[pollutant],
                               mode='lines+markers',
                               name='Monthly Average'))

    # Updating layout
    fig.update_layout(title=f'Monthly Trend Analysis for {pollutant}',
                      xaxis_title='Month',
                      yaxis_title=f'{pollutant} Concentration',
                      xaxis_tickangle=-45)

    return fig

def create_monthly_trend_analysis_all_layout(df):
    return html.Div([
        dcc.Graph(
            id='monthly-trend-analysis-all',
            figure=monthly_trend_analysis_all(df, 'PM10')
        )
    ])