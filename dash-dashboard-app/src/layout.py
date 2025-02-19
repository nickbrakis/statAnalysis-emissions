from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div([
    html.H1("PM10 Concentration Dashboard"),
    
    dcc.Dropdown(
        id='plot-type-dropdown',
        options=[
            {'label': 'Daily Concentrations', 'value': 'daily'},
            {'label': 'Monthly Concentrations', 'value': 'monthly'},
            {'label': 'Annual Concentrations', 'value': 'annual'},
            {'label': 'Monthly Distribution', 'value': 'monthly_distribution'},
            {'label': 'Weekly Distribution', 'value': 'weekly_distribution'},
            {'label': 'Monthly Trend Analysis', 'value': 'monthly_trend'},
            {'label': 'Hourly Distribution', 'value': 'hourly_distribution'},
            {'label': 'Mean PM10 by Day of Week', 'value': 'mean_day_of_week'},
            {'label': 'Mean PM10 by Year for Each Season', 'value': 'mean_season'},
            {'label': 'Annual Trend Analysis with CI', 'value': 'annual_trend_ci'},
        ],
        value='daily'
    ),
    
    dcc.Graph(id='graph-output'),
])

if __name__ == '__main__':
    app.run_server(debug=True)