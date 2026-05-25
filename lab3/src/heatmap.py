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
#     data = data.rename(columns={"Arrond_Nom": "Neighborhood","Date_Plantation": "Year","Counts": "Trees"})
#     print(data)
    
        
    # heatmap_data = data.pivot_table(index="Neighborhood",columns="Year",values="Trees",aggfunc="sum",fill_value=0)
    heatmap_data = data
    fig = px.imshow(heatmap_data,x=heatmap_data.columns,y=heatmap_data.index,color_continuous_scale="Viridis",labels=dict(x="Year", y="Neighborhood", color="Trees"),aspect="auto")

    #Make sure to set dragmode=False in
    fig.update_layout(dragmode=False)

    fig.update_xaxes(tickmode="array",tickvals=list(heatmap_data.columns),ticktext=list(heatmap_data.columns))
    #Also don't forget to include the hover template.
    fig.update_traces(hovertemplate=hover_template.get_heatmap_hover_template()
)


    return fig
    #return None

