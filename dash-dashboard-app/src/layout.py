from dash import dcc, html

def create_layout():
    return html.Div([
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            multiple=True
        ),
        dcc.Dropdown(
            id='plot-selector',
            options=[
                {'label': 'Daily Concentrations', 'value': 'daily_concentrations'},
                {'label': 'Monthly Concentrations', 'value': 'monthly_concentrations'},
                # Add more plot options here
            ],
            placeholder="Select a plot"
        ),
        html.Div(id='output-plot')
    ])