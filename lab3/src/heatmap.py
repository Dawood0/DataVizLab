'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template
import pandas as pd


def get_figure(data):

    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''

    # TODO : Create the heatmap. Make sure to set dragmode=False in
    # the layout. Also don't forget to include the hover template.


    fig = px.imshow(data, x=data.columns , y=data.index , color_continuous_scale="Viridis")
    
    fig.update_layout( dragmode=False, xaxis_title="Year", yaxis_title="Neighborhood", coloraxis_colorbar_title="Trees")
    
    fig.update_xaxes(tickmode="array", tickvals=list(data.columns))
    
    fig.update_traces(hovertemplate = hover_template.get_heatmap_hover_template())

    fig.show()
    
    return fig
    #return None

def main():
    data = pd.read_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab3\src\assets\data\arbres.csv",index_col=0)

    fig = get_figure(data)
    fig.show()


if __name__ == "__main__":
    main()