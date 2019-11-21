# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    dbc.Row([
        dcc.Markdown(
            """
        
            ## Predict reviewer characteristics 

           We browse yelp because we want to see what customers have to say about restaurants and other businesses.
           But what do we have to say about customers? Is a reviewer really a customer? 
           
           See that one-star review? Don't take it personally. The average rating for that reviewer is 
           is 1.2. 

           This user left a really long review, I wonder if they normally do that? 

           How do ratings differ when we look at different Zip Codes?

            """
        ),
        dcc.Link(dbc.Button("Predict", color='primary'), href='/predictions')
    ,
    ])
)

import pandas as pd 


dataset = pd.read_csv('assets/yelp_sample_dataset.csv')
fig2 = px.scatter_3d(dataset, x='year_joined', y='text_length', z='stars_business', color='average_stars')

fig2.update_layout(
     width=1200,
    height=1200
)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig2)
    ]
)

layout = dbc.Row([column1, column2])