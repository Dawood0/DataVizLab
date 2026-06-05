'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
from dash import html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    if style['visibility'] == 'hidden':
        return "", "", "", style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    if style['visibility'] == 'hidden':
        return "", "", "", style
    else:
        return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
    
    #need to define color
    # title = html.Span(title_text, style={'color': color, 'fontWeight': 'bold'})
    title_text = figure['data'][curve]['text'][point]
    color = figure['data'][curve]['marker']['color']
    title = html.Span(title_text, style= {'color':color})
    # title = html.Span(title_text, style= {'color':color, 'fontWeight':'bold'})
    mode_text = figure['data'][curve]['customdata'][point][0]
    mode = [html.Span(mode_text, style={'fontWeight': 'bold'}), html.Br()]
    
    theme_text = figure['data'][curve]['customdata'][point][1]
    theme = ([html.Span("Thématique:"), html.Ul(children=[html.Li(text) for text in theme_text.split('\n')])] if theme_text else None)
    
    style['visibility'] = 'visible'
     
    return title, mode, theme, style
