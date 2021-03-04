import pandas as pd
import plotly.express as px
from datetime import datetime as dt
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


########### Initiate the app
#---------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle


########### Get Data
#---------------------------------------------------------------
df = pd.read_csv('/content/drive/MyDrive/revenue_worm.csv')


########### Set up the layout
#---------------------------------------------------------------
app.layout = html.Div([
    html.H3("Usage Revenue", style={'textAlign': 'center'}),
    dcc.DatePickerRange(
        id='my-date-picker-range',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(2021, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2021, 12, 31),  # maximum date allowed on the DatePickerRange component
        initial_visible_month=dt(2021, 3, 1),  # the month initially presented when the user opens the calendar
        start_date=dt(2021, 3, 1).date(),
        end_date=dt(2021, 3, 1).date(),
        display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
        month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
        minimum_nights=0,  # minimum number of days between start and end date

        persistence=True,
        persisted_props=['start_date'],
        persistence_type='session',  # session, local, or memory. Default is 'local'

        updatemode='singledate'  # singledate or bothdates. Determines when callback is triggered
    ),

    
    dcc.Graph(id='mymap')
])

########### Set up callbacks
#------------------------------------------------------------------
@app.callback(
    Output('mymap', 'figure'),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date')]
)
def update_output(start_date, end_date):
        
    data = df.loc[(df["Date"] >= start_date) & (df["Date"] <= end_date)]
    
    fig = px.bar(data, x=data['WiFi Zone'], y=data['Total Revenue'], hover_data = [data['Date']],
            color=data['Location'],labels={'y':'Usage Revenue','x':"WiFi Zone",'color':"Location","hover_data_0":"Date"},
            color_discrete_sequence= px.colors.sequential.Darkmint_r,
            template='plotly_white')
    fig.update_layout( xaxis_tickangle=-40, xaxis={'categoryorder':'total descending'},xaxis_title_text='WiFi Zone', 
      yaxis_title_text='Usage Revenue',xaxis_showticklabels=False,
      )
    fig.update_yaxes(tickprefix="R")
    fig.show()
    
    return fig

#------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server()
