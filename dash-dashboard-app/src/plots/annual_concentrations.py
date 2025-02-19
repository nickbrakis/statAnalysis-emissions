from dash import dcc, html
import plotly.graph_objs as go

def annual_concentration_plot(df, pollutant):
    annual_data = df.groupby(df['date'].dt.year)[pollutant].mean().reset_index()
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=annual_data['date'],
        y=annual_data[pollutant],
        mode='lines+markers',
        name=f'Annual Average {pollutant}',
        line=dict(shape='linear')
    ))
    
    fig.update_layout(
        title=f'Annual Average Concentration of {pollutant}',
        xaxis_title='Year',
        yaxis_title='Concentration',
        template='plotly_white'
    )
    
    return fig