from dash import dcc, html
import plotly.express as px
import pandas as pd

def mean_pm10_by_day_of_week(df):
    # Calculate mean PM10 concentrations by day of the week
    df['day_of_week'] = df['date'].dt.day_name()
    mean_values = df.groupby('day_of_week')['PM10'].mean().reset_index()

    # Create a Plotly bar chart
    fig = px.bar(mean_values, x='day_of_week', y='PM10',
                 title='Mean PM10 Concentrations by Day of the Week',
                 labels={'day_of_week': 'Day of the Week', 'PM10': 'Mean PM10 Concentration'},
                 color='PM10', 
                 color_continuous_scale=px.colors.sequential.Viridis)

    return fig