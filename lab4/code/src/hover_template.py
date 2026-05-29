'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    return (
        "<b>Country</b>: %{hovertext}<br>"
        "<b>Population</b>: %{marker.size:,.0f}<br>"
        "<b>GDP</b>: $%{x:,.0f}<br>"
        "<b>CO2 emissions</b>: %{y:,.2f} tonnes"
        "<extra></extra>"
    )
