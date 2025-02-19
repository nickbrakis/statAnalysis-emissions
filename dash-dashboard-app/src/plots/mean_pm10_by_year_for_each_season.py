from dash import dcc, html
import plotly.express as px
import pandas as pd

def mean_pm10_by_year_for_each_season(df):
    # Assuming df has a 'year', 'season', and 'PM10' columns
    seasonal_means = df.groupby(['year', 'season'])['PM10'].mean().reset_index()

    fig = px.bar(seasonal_means, 
                 x='year', 
                 y='PM10', 
                 color='season', 
                 title='Mean PM10 Concentrations by Year for Each Season',
                 labels={'PM10': 'Mean PM10 Concentration', 'year': 'Year'},
                 barmode='group')

    return dcc.Graph(figure=fig)