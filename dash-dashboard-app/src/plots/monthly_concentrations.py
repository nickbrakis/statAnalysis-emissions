from plotly import graph_objs as go
import pandas as pd

def monthly_concentrations(df, pollutant):
    monthly_data = df.resample('M').mean()[pollutant]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=monthly_data.index, y=monthly_data, mode='lines+markers', name=pollutant))
    
    fig.update_layout(
        title=f'Monthly Average Concentrations of {pollutant}',
        xaxis_title='Month',
        yaxis_title='Concentration',
        template='plotly'
    )
    
    return fig