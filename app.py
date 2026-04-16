from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("./formatted_data.csv")
df = df.sort_values(by="date")

fig = px.line(
    df, 
    x="date", 
    y="sales", 
    title="Pink Morsel Sales Over Time",
    labels={"date": "Date of Sale", "sales": "Total Sales ($)"}
)

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Visualiser',
        style={'textAlign': 'center', 'color': '#2c3e50'}
    ),

    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)