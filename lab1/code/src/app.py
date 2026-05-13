
# -*- coding: utf-8 -*-

'''
    File name: app.py
    Author: Olivia Gélinas
    Course: INF8808
    Python Version: 3.8

    This file contains the entry point for TP1.
'''

import dash
# from dash_core_components import Graph
# import dash_html_components as html
# these commented were giving errors so they were replaced 


from dash import dcc 
from dash import html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go
import plotly.io as pio

import pandas as pd
import numpy as np
import random


app = dash.Dash(__name__)
app.title = 'TP1 | INF8808'


def generate_data():
    '''
		Generates random data to be displayed in the scatter plot.

		The data must be a 2 X m array of randomly generated (x, y) coordinates, with :
			- x : an integer in [1, 99],
			- y : an integer in [1, 99],

		and where m is a random number in [1, 10].   

		For example, the coordinates could be :
            x  |  y
          ----------
            99 | 4
            27 | 89
            17 | 42
    Returns:
		A pandas dataframe with columns 'x' and 'y' containing the randomly
		generated coordinate data.
    '''
    ####my code
    m = random.randint(1, 11)
    x = np.random.randint(1, 100, m)
    y = np.random.randint(1, 100, m)
    return pd.DataFrame({'x': x, 'y': y})
    ####end my code



def get_layout():
    '''
    
        Gets the Graph Object-formatted Layout used for the figure.

        Returns:
            The Layout object describing the overall visual appearance of the graph.
    '''
    return go.Layout(
        title=dict(text='Mon premier graphique', xanchor='center', x=0.5),
        font_family='Helvetica',
        font_color='#000000',
        xaxis_title='Axe x',
        xaxis_range=[0, 100],
        yaxis_title='Axe y',
        yaxis_range=[0, 100],
        template=pio.templates['simple_white']
    )


def init_figure(dataframe, layout):
    '''
        Initializes the Graph Object-formatted figure to display in the graph.

        The figure's data is initialised as a Scatter graph object. The mode is "markers" and
        their color is "#07BEB8". Their size is 10.

        See link :
             https://plotly.com/python/creating-and-updating-figures/#figures-as-graph-objects

        Args:
            dataframe: The data to display in the figure.
            layout: The layout used in the figure.
        Returns:
            The Graph Object-formatted figure to be displayed.
    '''
    ####my code
    return go.Figure(
        data=go.Scatter(
            x=dataframe['x'],
            y=dataframe['y'],
            mode='markers',
            marker=dict(color='#07BEB8', size=10)
        ),
        layout=layout
    )
    ####end my code


def init_app_layout(figure):
    '''
        Generates the HTML layout representing the app.

        Args:
            figure: The figure to display.
        Returns:
            The HTML structure of the app's web page.
    '''
    return html.Div(children=[
        ####my code
        html.Div(children=[
            html.H1('TP1'),
            html.Div('Bienvenue au cours INF8808 : Visualisation de données.')
        ]),
        ####end my code
        html.Main(children=[
            html.Div(id='viz-group', children=[
                dcc.Graph(
                    id='example-graph',
                    figure=figure,
                    config={
                        'staticPlot': True
                    }
                ),
                html.Div(className='info-panel', children=[
                    html.Div(id='info-text'),
                    html.Button('Actualiser', id='update-btn')
                ])
            ])
        ])
    ])


def update_figure(figure):
    '''
        Updates the figure by regenerating the random data to display.

        Args:
            figure: The figure to update.
        Returns:
            updated_fig: The figure with updated data.
    '''

    updated_df = generate_data()

    figure = go.Figure(figure) # conversion back to Graph Object
 
    if not updated_df.empty:
        figure.update_traces(x=updated_df.x, y=updated_df.y)

    return figure


def update_label(figure):
    '''
        Updates the information panel  displayed under the graph. It shows
        the number of points that are currently displayed in the graph.

        Args:
            figure: The figure to be displayed
        Returns:
            label_elements: The information elements to display
            under the graph, where the number of points is displayed in bold.
    '''

    figure = go.Figure(figure) # conversion back to Graph Object

    ####my code
    n = 0
    if len(figure.data) > 0 and figure.data[0].x is not None:
        n = len(figure.data[0].x)
    return [
        html.Span('there are : '),
        html.Strong(str(n)),
        html.Span(' point' if n == 1 else ' points')
    ]
    ####end my code


@app.callback(
    [Output('example-graph', 'figure'), Output('info-text', 'children')],
    [Input('update-btn', 'n_clicks')],
    [State('example-graph', 'figure')]
)
def button_clicked(n_clicks, figure):
    '''
        Updates the application after a click on the 'Actualiser' button.

        Args:
            n_clicks: The number of times the buttton has been clicked so far
            figure: The figure as it is currently displayed
        Returns:
            figure: The figure to display after the click on the 'Actualiser' button
            label_content: The new content to display in the information panel
    '''

    if n_clicks is not None:
        figure = update_figure(figure)

    label_content = update_label(figure)

    return figure, label_content


lyt = get_layout()

df = generate_data()

fig = init_figure(df, lyt)

app.layout = init_app_layout(fig)

####my code
if __name__ == '__main__':
    app.run(debug=True)
####end my code
