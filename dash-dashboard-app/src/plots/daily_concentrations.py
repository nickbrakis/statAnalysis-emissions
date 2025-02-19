from dash import dcc, html
import plotly.express as px

def daily_concentration_plot(df):
    fig = px.line(df, x='date', y='PM10', title='Daily PM10 Concentrations')
    fig.update_layout(xaxis_title='Date', yaxis_title='PM10 Concentration (µg/m³)')
    return dcc.Graph(figure=fig)