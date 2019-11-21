import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from app import app

import pandas as pd
from joblib import load
pipeline = load('assets/pipeline.joblib')


column1 = dbc.Col([html.H1('Prediction:', className='mb-5')])

column2 = dbc.Col([
     html.Div(id='output-state')
    ])


column3 = html.Div(className='row',
children=[dbc.Col([
    html.Div(dcc.Input(id='input-1-state', type='number', value='2018')),
    html.Div(dcc.Input(id='input-2-state', type='number', value='3.0')),
    html.Div(dcc.Input(id='input-3-state', type='number', value='5')), 
    html.Div(html.Button(id='submit-button', n_clicks=0, children='Submit')),
])])






layout = dbc.Row([column1, column2, column3])

# layout = html.Div([
#     dcc.Input(id='input-1-state', type='text', value='2018'),
#     dcc.Input(id='input-2-state', type='text', value='3.0'),
#     dcc.Input(id='input-3-state', type='text', value='5'),
#     html.Button(id='submit-button', n_clicks=0, children='Submit'),
#     html.Div(id='output-state')
# ])


@app.callback(Output('output-state', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('input-1-state', 'value'),
               State('input-2-state', 'value'),
               State('input-3-state', 'value')])
def update_output(n_clicks, input1, input2, input3):
    df = pd.DataFrame(
    columns=['input1', 'input2', 'input3'], 
    data=[[input1, input2, input3]]
    )
    y_pred = pipeline.predict(df)[0]
    f'{y_pred:.0f} text_length'
    return u'''
        For a user that joined in {},
        where the average number of stars they give is {},
        and the number of reviews they have is {}, 
        then we predict their review is approximately {:.0f} characters long.
        
    '''.format(input1, input2, input3, y_pred)


# column1 = dbc.Col([
#     dcc.Input(id='year_joined-state', value='2018', type='text'),
#     # html.Div(id='my-div'),
#     dcc.Input(id='average_stars-state', value='3.0', type='text'),
#     dcc.Input(id='user_review_count-state', value='7', type='text'),
#     html.Button(id='submit-button', n_clicks=0, children='Submit'),
#     html.Div(id='output-state')
# ])



# column2 = dbc.Col([
#         html.H2('Expected Length', className='mb-5'), 
#         html.Div(id='predict-state', className='lead')
#     ])


# @app.callback(Output('predict-state', 'children'),
#     [Input('submit-button', 'n_clicks')], 
#     [State('year_joined', 'value'),
#     State('average_stars', 'value'),
#     State('user_review_count', 'value')])

# def update_predict(n_clicks, year_joined, average_stars, user_review_count):
#     df = pd.DataFrame(
#     columns=['year_joined', 'average_stars', 'user_review_count'], 
#     data=[[year_joined, average_stars, user_review_count]]
#     )

#     y_pred = pipeline.predict(df)[0]
#     return f'{y_pred:.0f} text_length'



# layout = dbc.Row([column1, column2])

# if __name__ == "__main__":
#     app.run_server(debug=True)






