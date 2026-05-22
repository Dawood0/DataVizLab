'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    fig = px.scatter()
    add_rectangle_shape(fig)

    fig.add_annotation(
        text='No data to display. Select a cell<br>in the heatmap for more information.',
        x=0.5,
        y=0.5,
        xref='paper',
        yref='paper',
        showarrow=False
    )
    fig.update_layout(
        dragmode=False,
        xaxis_visible=False,
        yaxis_visible=False
    )
    return fig
    # return None


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    fig.add_shape(
        type='rect',
        xref='paper',
        yref='paper',
        x0=0,
        x1=1,
        y0=0.25,
        y1=0.75,
        fillcolor=THEME['pale_color'],
        line_width=0
    )
    return fig
    # return None


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    if line_data is None or len(line_data) == 0:
        return get_empty_figure()

    fig = px.line(
        line_data,
        x='Date_Plantation',
  y='Counts',
          title='Trees planted in ' + str(arrond) + ' in ' + str(year)
    )

    if len(line_data) == 1:
        fig.update_traces(mode='markers')
    fig.update_traces(
        hovertemplate=hover_template.get_linechart_hover_template()
    )
    fig.update_xaxes(tickformat='%d %b')
    fig.update_yaxes(title='Counts')
    fig.update_layout(dragmode=False)

    return fig
    # return None




# if __name__ == "__main__":
    from pathlib import Path
    import pandas as pd

    from preprocess import (
        convert_dates,
        filter_years,
        get_daily_info
    )

    DATA_DIR = Path(__file__).resolve().parent / "assets" / "data"
    dataframe = pd.read_csv(DATA_DIR / "arbres.csv")
    dataframe = convert_dates(dataframe)
    dataframe = filter_years(dataframe, 2010, 2020)

    line_data = get_daily_info(
        dataframe,
        "Ahuntsic - Cartierville",
        2010
    )

    # renaming the columns for testing
    line_data.columns = ["Date_Plantation", "Counts"]

    fig = get_figure(
        line_data,
        "Ahuntsic - Cartierville",
        2010
    )

    fig.show()