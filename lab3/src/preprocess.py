'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd


def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe["Date_Plantation"] = pd.to_datetime(dataframe["Date_Plantation"])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    dataframe = dataframe[dataframe["Date_Plantation"].dt.year.between(start, end)]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    counts = dataframe.groupby(["Arrond_Nom", dataframe["Date_Plantation"].dt.year]).size().reset_index(name="Counts")
    return counts


def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    restructured = yearly_df.pivot(index="Arrond_Nom", columns="Date_Plantation", values="Counts").fillna(0)
    return restructured


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
    filtered = dataframe[
        (dataframe["Arrond_Nom"] == arrond) &
        (dataframe["Date_Plantation"].dt.year == year)
    ]

    daily = (filtered.groupby("Date_Plantation").size().reset_index(name="Counts")
    )

    # create full date range for the year
    full_range = pd.date_range(start=f"{year}-01-01", end=f"{year}-12-31")

    daily = daily.set_index("Date_Plantation").reindex(full_range, fill_value=0)

    daily = daily.rename_axis("Date_Plantation").reset_index()    
    return daily


# if __name__ == "__main__":
#     from pathlib import Path
#     DATA_DIR = Path(__file__).resolve().parent / "assets" / "data"

#     dataframe = pd.read_csv(DATA_DIR / 'arbres.csv')
    
#     dataframe = convert_dates(dataframe)
#     dataframe.to_csv(DATA_DIR / 'datetime-formatted.csv')
    
#     dataframe = filter_years(dataframe, 2010, 2020)
#     dataframe.to_csv(DATA_DIR / 'date-filtered.csv')
    
#     yearly_df = summarize_yearly_counts(dataframe)
#     yearly_df.to_csv(DATA_DIR / 'yearly-counts.csv')

#     data = restructure_df(yearly_df)
#     data.to_csv(DATA_DIR / 'restructured.csv')
    
#     line_data = get_daily_info(dataframe, "Ahuntsic - Cartierville", 2010)
#     line_data.to_csv(DATA_DIR / 'line-data.csv')
