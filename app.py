from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

df = pd.read_csv("./formatted_data.csv")
df = df.sort_values(by="date")

app = Dash(__name__)

app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'padding': '50px', 'fontFamily': 'sans-serif'}, children=[
    
    html.H1(
        children='Pink Morsel Sales Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50', 'marginBottom': '30px'}
    ),

    html.Div(style={'textAlign': 'center', 'marginBottom': '20px'}, children=[
        html.Label("Select Region: ", style={'fontWeight': 'bold', 'marginRight': '100px'}),
        dcc.RadioItems(
            id='region-picker',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', 
            inline=True,
            inputStyle={"margin-left": "20px"}
        ),
    ]),

    html.Div(style={'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'boxShadow': '0px 4px 6px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(id='sales-line-chart')
    ])
])

@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-picker', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'] == selected_region]

    fig = px.line(
        filtered_df, 
        x="date", 
        y="sales", 
        title=f"Pink Morsel Sales - {selected_region.upper()} Region",
        template="plotly_white" # Makes the graph look cleaner
    )
    
    fig.update_layout(transition_duration=500) # Smooth animation
    return fig

if __name__ == '__main__':
    app.run(debug=True)