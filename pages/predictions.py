# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout


import pandas as pd

dataset = pd.read_csv('assets/yelp_sample_dataset.csv')

from sklearn.model_selection import train_test_split
train, test = train_test_split(dataset, test_size =0.1, shuffle=True, random_state=42)

# train.shape, test.shape

# target = "average_stars_class"
# X_train = train.drop(columns=[target, 'average_stars'])
# y_train = train[target]
# X_test = test.drop(columns=[target, 'average_stars'])
# y_test = test[target]

# from sklearn.pipeline import make_pipeline
# import category_encoders as ce
# from sklearn.impute import SimpleImputer
# transformers = make_pipeline(
#     ce.OrdinalEncoder(),
#     SimpleImputer(strategy='median')
# )
# X_train_T = transformers.fit_transform(X_train)
# X_test_T = transformers.transform(X_test)

# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train_T, y_train) 
# print("Model Score: ", model.score(X_test_T, y_test))


from sklearn.externals import joblib
import plotly.graph_objs as go


if __name__ == '__main__':
    app.run_server(debug=True)

    app.layout = html.Div(children=[
    html.H1(children='Simple Linear Regression', style={'textAlign': 'center'}),

    html.Div(children=[
        html.Label('Enter years of experience: '),
    ], style={'textAlign': 'center'}),
])


dcc.Input(id='years-of-experience', placeholder='Years of experience', type='text')


if __name__ == '__main__':
    model = joblib.load("./linear_regression_model.pkl")
    app.run_server(debug=True)


@app.callback(
    Output(component_id='result', component_property='children'),
    [Input(component_id='years-of-experience', component_property='value')])
def update_years_of_experience_input(years_of_experience):
    pass


@app.callback(
    Output(component_id='result', component_property='children'),
    [Input(component_id='years-of-experience', component_property='value')])
def update_years_of_experience_input(years_of_experience):
    if years_of_experience is not None and years_of_experience is not '':
        try:
            salary = model.predict(float(years_of_experience))[0]
            return 'With {} years of experience you should earn a salary of ${:,.2f}'.                format(years_of_experience, salary, 2)
        except ValueError:
            return 'Unable to give years of experience'



training_data = train
training_labels = train.columns



dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                go.Scatter(
                    x=training_data['YearsExperience'],
                    y=training_labels,
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                )
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'Years of Experience'},
                yaxis={'title': 'Salary'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                hovermode='closest'
            )
        }
    )