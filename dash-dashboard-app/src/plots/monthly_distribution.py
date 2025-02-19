from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_monthly_distribution_plot(df, pollutant):
    monthly_data = df.groupby(df['date'].dt.to_period('M'))[pollutant].mean().reset_index()
    monthly_data['date'] = monthly_data['date'].dt.to_timestamp()

    fig = px.bar(monthly_data, x='date', y=pollutant,
                 title=f'Monthly Distribution of {pollutant}',
                 labels={'date': 'Month', pollutant: f'Average {pollutant}'})

    return fig