from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_hourly_distribution_plot(df, pollutant='PM10'):
    # Group by hour and calculate mean concentration
    hourly_data = df.groupby(df['timestamp'].dt.hour)[pollutant].mean().reset_index()
    hourly_data.columns = ['Hour', 'Mean Concentration']

    # Create the Plotly figure
    fig = px.line(hourly_data, x='Hour', y='Mean Concentration', 
                  title=f'Hourly Distribution of {pollutant} Concentrations',
                  labels={'Hour': 'Hour of the Day', 'Mean Concentration': f'Mean {pollutant} Concentration'},
                  markers=True)

    return fig

def hourly_distribution_layout():
    return html.Div([
        dcc.Graph(id='hourly-distribution-graph')
    ])