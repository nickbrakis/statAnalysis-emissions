from dash import dcc, html
import plotly.express as px
import pandas as pd

def create_monthly_trend_analysis_single_month_plot(df, month):
    # Filter the DataFrame for the specified month
    df_filtered = df[df['month'] == month]
    
    # Create a line plot for the monthly trend analysis
    fig = px.line(df_filtered, x='year', y='PM10', title=f'Monthly Trend Analysis for Month {month}')
    
    return fig

def layout(df):
    return html.Div([
        dcc.Dropdown(
            id='month-dropdown',
            options=[{'label': str(i), 'value': i} for i in range(1, 13)],
            value=1,
            clearable=False
        ),
        dcc.Graph(id='monthly-trend-graph', figure=create_monthly_trend_analysis_single_month_plot(df, 1))
    ])

def register_callbacks(app, df):
    @app.callback(
        Output('monthly-trend-graph', 'figure'),
        Input('month-dropdown', 'value')
    )
    def update_graph(selected_month):
        return create_monthly_trend_analysis_single_month_plot(df, selected_month)