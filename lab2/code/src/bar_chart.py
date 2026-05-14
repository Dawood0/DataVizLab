'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN


def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    base_template = 'simple_white'
    custom_template = 'custom_theme'
    template = (
        f'{base_template}+{custom_template}'
        if custom_template in pio.templates
        else pio.templates[base_template]
    )

    fig.update_layout(
        template=template,
        title='Lines per Act',
        dragmode=False,
        barmode='relative'
    )
    
    
    
def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode
    
    data["Lines"] = (
    data.groupby(["Act", "Player"])["Line"].transform("count"))

    mode = "Lines"

    fig = go.Figure(fig)  # conversion back to Graph Object
    fig.data = []


    for player in data["Player"].unique():

        player_data = data[data["Player"] == player]

        fig.add_trace(
            go.Bar(
                x=player_data["Act"],
                y=player_data[mode],
                name=player
            )
        )
    fig.show()
    
    return fig


def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    
    data["Lines"] = (data.groupby(["Act", "Player"])["Line"].transform("count"))
    data["Lines%"] = ((data.groupby(["Act", "Player"])["Line"].transform("count"))/ data.groupby("Act")["Line"].transform("count")) * 100

    #pick between count of percent
    whichone = "count"

    if whichone == "percent":
            fig.update_yaxes(title_text="Lines as a percentage")
            mode = "Lines%"

    else:
        fig.update_yaxes(title_text="Lines as a count")
        mode = "Lines"


    fig = go.Figure(fig)  # conversion back to Graph Object
    fig.data = []


    for player in data["Player"].unique():

        player_data = data[data["Player"] == player]

        fig.add_trace(
            go.Bar(
                x=player_data["Act"],
                y=player_data[mode],
                name=player
            )
        )
    fig.show()



if __name__ == "__main__":

    import pandas as pd

    # Read data
    data = pd.read_csv(
        r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\romeo_and_juliet.csv"
    )

    # Initialize figure
    fig = init_figure()

    # Choose mode
    mode = "Lines"

    # Draw chart
    fig = draw(fig, data, mode)

    # Update y axis
    fig = update_y_axis(fig, mode)

    # Show chart
    fig.show()