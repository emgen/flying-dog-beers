import pandas as pd
import plotly.express as px

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

########### Define your variables

cust_dff= pd.read_csv("Cust_df.csv")

########### Set up the chart


fig = px.line(
    y= cust_dff['Customer Count'] , # name used in legend and hover labels
    x=cust_dff['Date'],labels={'y':'No. Customers','x':"Date" })

fig.update_layout(
    title_text='Active Customer Report', # title of plot
    xaxis_tickangle=-45,xaxis_title_text='Date', 
    yaxis_title_text='Number of Customers')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure= fig
    ),
    ]
)

if __name__ == '__main__':
    app.run_server()
