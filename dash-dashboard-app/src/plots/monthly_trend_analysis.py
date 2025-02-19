from dash import dcc, html
import plotly.graph_objs as go

def monthly_trend_analysis(df, pollutant):
    monthly_data = df.groupby(df['date'].dt.to_period('M')).mean()[pollutant]
    
    figure = go.Figure()
    figure.add_trace(go.Scatter(
        x=monthly_data.index.astype(str),
        y=monthly_data.values,
        mode='lines+markers',
        name='Monthly Average',
        line=dict(shape='linear')
    ))
    
    figure.update_layout(
        title=f'Monthly Trend Analysis for {pollutant}',
        xaxis_title='Month',
        yaxis_title=f'Average {pollutant} Concentration',
        template='plotly_white'
    )
    
    return figure