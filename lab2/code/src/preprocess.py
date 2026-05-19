'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from pathlib import Path
from modes import MODE_TO_COLUMN

import pandas as pd

DATA_DIR = Path(__file__).resolve().parent / "assets" / "data"


def summarize_lines(my_df):

    '''
        Sums each player's total of number of lines and  its
        corresponding percentage per act.

        The sum of lines per player per act is in a new
        column named 'PlayerLine'.

        The percentage of lines per player per act is
        in a new column named 'PlayerPercent'

        Args:
            my_df: The pandas dataframe containing the data from the .csv file
        Returns:
            The modified pandas dataframe containing the
            information described above.
    '''
    # TODO : Modify the dataframe, removing the line content and replacing
    # it by line count and percent per player per act

    # READ THE DATA
    my_df = pd.read_csv(DATA_DIR / "romeo_and_juliet.csv")


    # NUMBER OF LINES PER PLAYER
    player_lines_count = my_df.groupby("Player")["Line"].count()
    # print(player_lines_count.head())

   
    #GROUPBY
    my_df.to_csv(DATA_DIR / "my_df_1.csv",index=False)
    my_df = my_df.drop(columns=["Scene"])
    my_df = (my_df.groupby(["Act", "Player"], as_index=False)["Line"].count())
    my_df.to_csv(DATA_DIR / "my_df_2.csv",index=False)
    
    #NUMBER OF LINE PER PLAYER PER ACT IN A NEW COLUMN
    my_df["PlayerLine"] = my_df.groupby(["Act", "Player"])["Line"].transform("sum")


    #PERCENTAGE OF LINE PER PLAYER PER ACT IN A NEW COLUMN
    my_df["PlayerPercent"] = (my_df["PlayerLine"] / my_df.groupby("Act")["Line"].transform("sum") *100)


    my_df.to_csv(DATA_DIR / "my_df-FINAL_PART_1.csv",index=False)
    return my_df


def replace_others(my_df):
    '''
        For each act, keeps the 5 players with the most lines
        throughout the play and groups the other plyaers
        together in a new line where :

        - The 'Act' column contains the act
        - The 'Player' column contains the value 'OTHER'
        - The 'LineCount' column contains the sum
            of the counts of lines in that act of
            all players who are not in the top
            5 players who have the most lines in
            the play
        - The 'PercentCount' column contains the sum
            of the percentages of lines in that
            act of all the players who are not in the
            top 5 players who have the most lines in
            the play

        Returns:
            The df with all players not in the top
            5 for the play grouped as 'OTHER'
    '''
    # TODO : Replace players in each act not in the top 5 by a
    # new player 'OTHER' which sums their line count and percentage


    #SORT BY ACT IN ASCENDING ORDER
    # my_df = my_df.sort_values(["Act","PlayerLine"], ascending = [True,False])
    my_df = my_df.sort_values(["PlayerLine"], ascending = False)
    my_df.to_csv(DATA_DIR / "my_dfPart2.csv",index=False)
    
    #RANK EACH player for the entire play
    my_df_ranked_and_grouped_by = my_df.groupby("Player", as_index=False)[["Line", "PlayerLine", "PlayerPercent"]].sum().assign(Rank=lambda df: df["PlayerLine"].rank(method="first", ascending=False).astype(int)).sort_values("Rank")
    my_df["Rank"] = my_df["PlayerLine"].rank(method = "first", ascending = False)
    my_df_ranked_and_grouped_by.to_csv(DATA_DIR / "my_dfPart2_v1_1.csv",index=False)

    my_df_ranked_and_grouped_by["Are you OTHER"] = ""
    my_df_ranked_and_grouped_by.loc[my_df_ranked_and_grouped_by["Rank"] > 5, "Are you OTHER"] = "OTHER"
    my_df_ranked_and_grouped_by.to_csv(DATA_DIR / "my_df-FINAL_list_other.csv",index=False)
    my_df_1 = my_df_ranked_and_grouped_by[my_df_ranked_and_grouped_by["Are you OTHER"] == "OTHER"]
    my_df_1.to_csv(DATA_DIR / "my_df-FINAL_PART_2.csv",index=False)
    my_df.loc[my_df["Player"].isin(my_df_1["Player"]), "Player"] = "OTHER"

    ## PUT THE ONES AFTER RANK=5 IN CATEGORY OTHER , replace their names with OTHER
    my_df_ranked_and_grouped_by.loc[my_df_ranked_and_grouped_by["Are you OTHER"] == "OTHER", "Player"] = "OTHER"
    my_df_ranked_and_grouped_by = my_df_ranked_and_grouped_by.drop(columns=["Are you OTHER"])
    my_df_ranked_and_grouped_by = my_df_ranked_and_grouped_by.groupby(["Player"], as_index=False)[["Line", "PlayerLine", "PlayerPercent"]].sum()
    my_df_ranked_and_grouped_by.to_csv(DATA_DIR / "my_dfPart2_v3.csv",index=False)

    return my_df

def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    
    my_df["Player"] = my_df["Player"].str.title()
    my_df = my_df.groupby(["Act", "Player"], as_index=False)[["Line", "PlayerLine", "PlayerPercent"]].sum()
    my_df.to_csv(DATA_DIR / "my_df-FINAL_PART_3.csv",index=False)
    # print(my_df) 
    
    
    
       
    return my_df
