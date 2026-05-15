'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
from pathlib import Path
from template import create_template
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
        barmode='stack',
        xaxis = dict(type= "category")
    )
    
    return fig
    
    
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
    fig.data = []

    for player in data["Player"].unique():
       player_data = data[data["Player"]== player] 
       
       fig.add_trace(
           go.Bar(
               x = player_data["Act"],
               y = player_data[MODE_TO_COLUMN[MODES[mode]]],
               name=player,
                # hovertemplate=get_hover_template(player, mode)
                hovertemplate=get_hover_template(player, mode)

           )
       )
    # fig.show()
    
    return fig



def update_y_axis(fig, data, mode='Count'):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    
    # PICK BETWEEN PERCENT OR COUNT 
    mode = MODES[mode]
    PlayerMode = MODE_TO_COLUMN[mode]



    fig = go.Figure(fig)  # conversion back to Graph Object

    if mode == "Percent":
        fig.update_yaxes(title_text="Lines (%)")
    else:
        fig.update_yaxes(title_text="Lines (Count)")

    fig.data = []


    for player in data["Player"].unique():

        player_data = data[data["Player"] == player]

        fig.add_trace(
            go.Bar(
                x=player_data["Act"],
                y=player_data[PlayerMode],
                name=player,
                hovertemplate=get_hover_template(player, mode)  # instead of 'whichone' it should be 'mode' we can change later 
            )
        )
    # fig.show()
    return fig



# if __name__ == "__main__":

#     mode = "Percent"
#     data_path = Path(__file__).resolve().parent / "assets" / "data" / "my_df-FINAL_PART_3.csv"
#     data = pd.read_csv(data_path)
#     fig = init_figure()
#     create_template()
#     fig = draw(fig, data, mode)
#     fig = update_y_axis(fig, mode)
#     fig.show()

    
