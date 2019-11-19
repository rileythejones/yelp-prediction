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
    [
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
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])