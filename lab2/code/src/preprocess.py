'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
from modes import MODE_TO_COLUMN

import pandas as pd


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
    my_df = pd.read_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\romeo_and_juliet.csv")
    print(my_df.head())

    print( "_______________________________________________")
    # NUMBER OF LINES PER PLAYER
    player_lines_count = my_df.groupby("Player")["Line"].count()
    print(player_lines_count.head())

    print( "_______________________________________________")
    #PERCENTAGE OF LINES PER PLAYER
    player_lines_percentages = my_df.groupby("Player")["Line"].count() / my_df["Line"].count() *100
    print(player_lines_percentages)

    print("the sum is " + str(player_lines_percentages.sum()))

    print( "_______________________________________________")
    #GROUPBY
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_df_1.csv",index=False)
    my_df = my_df.drop(columns=["Scene"])
    my_df = (my_df.groupby(["Act", "Player"], as_index=False)["Line"].count())
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_df_2.csv",index=False)
    
    #NUMBER OF LINE PER PLAYER PER ACT IN A NEW COLUMN
    my_df["PlayerLine"] = my_df.groupby(["Act", "Player"])["Line"].transform("sum")

    print( "_______________________________________________")
    #PERCENTAGE OF LINE PER PLAYER PER ACT IN A NEW COLUMN
    my_df["PlayerPercent"] = (my_df["PlayerLine"] / my_df.groupby("Player")["Line"].transform("sum") *100)

    print( "_______________________________________________")
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_df-FINAL_PART_1.csv",index=False)
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
    
    
    # ACT 1
    my_df_act_1 = my_df[my_df["Act"] == 1]
    print(my_df_act_1.head())

    lines_per_players_act_1= my_df_act_1.groupby("Player")["Line"].count().sort_values(ascending=False)
    print(lines_per_players_act_1.head())

    top_5_players_with_most_lines_act_1 = lines_per_players_act_1.head(5)

    print("This is the top 5 players with the most lines in act 1")
    sum_rest_of_players = lines_per_players_act_1.iloc[5:].sum()
    top_5_players_with_most_lines_act_1["OTHER"] = sum_rest_of_players

    #top_5_players_with_most_lines_act_1["PercentCount"] = (top_5_players_with_most_lines_act_1["LineCount"]/top_5_players_with_most_lines_act_1["LineCount"].sum()) * 100

    print(top_5_players_with_most_lines_act_1)

    # ACT 2
    my_df_act_2 = my_df[my_df["Act"] == 2]
    print(my_df_act_2.head())

    lines_per_players_act_2 = my_df_act_2.groupby("Player")["Line"].count().sort_values(ascending=False)
    print(lines_per_players_act_2.head())

    top_5_players_with_most_lines_act_2 = lines_per_players_act_2.head(5)

    print("This is the top 5 players with the most lines in act 2")
    sum_rest_of_players = lines_per_players_act_2.iloc[5:].sum()
    top_5_players_with_most_lines_act_2["OTHER"] = sum_rest_of_players
    print(top_5_players_with_most_lines_act_2)

    # ACT 3
    my_df_act_3 = my_df[my_df["Act"] == 3]
    print(my_df_act_3.head())

    lines_per_players_act_3 = my_df_act_3.groupby("Player")["Line"].count().sort_values(ascending=False)
    print(lines_per_players_act_3.head())

    top_5_players_with_most_lines_act_3 = lines_per_players_act_3.head(5)

    print("This is the top 5 players with the most lines in act 3")
    sum_rest_of_players = lines_per_players_act_3.iloc[5:].sum()
    top_5_players_with_most_lines_act_3["OTHER"] = sum_rest_of_players
    print(top_5_players_with_most_lines_act_3)


    # ACT 4
    my_df_act_4 = my_df[my_df["Act"] == 4]
    print(my_df_act_4.head())


    lines_per_players_act_4 = my_df_act_4.groupby("Player")["Line"].count().sort_values(ascending=False)
    print(lines_per_players_act_4.head())

    top_5_players_with_most_lines_act_4 = lines_per_players_act_4.head(5)

    print("This is the top 5 players with the most lines in act 4")
    sum_rest_of_players = lines_per_players_act_4.iloc[5:].sum()
    top_5_players_with_most_lines_act_4["OTHER"] = sum_rest_of_players
    print(top_5_players_with_most_lines_act_4)



    # ACT 5
    my_df_act_5 = my_df[my_df["Act"] == 5]
    print(my_df_act_5.head())

    lines_per_players_act_5 = my_df_act_5.groupby("Player")["Line"].count().sort_values(ascending=False)
    print(lines_per_players_act_5.head())

    top_5_players_with_most_lines_act_5 = lines_per_players_act_5.head(5)

    print("This is the top 5 players with the most lines in act 5")
    sum_rest_of_players = lines_per_players_act_5.iloc[5:].sum()
    top_5_players_with_most_lines_act_5["OTHER"] = sum_rest_of_players
    print(top_5_players_with_most_lines_act_5)
    
    
    ## ABOVE WAS A TEST HOW TO DO IT MANUALLY
    #SORT BY ACT IN ASCENDING ORDER
    my_df = my_df.sort_values(["Act","PlayerLine"], ascending = [True,False])
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_dfPart2.csv",index=False)
    
    #RANK EACH
    my_df["Rank"] = my_df.groupby("Act")["PlayerLine"].rank(method = "first", ascending = False)
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_dfPart2_v1.csv",index=False)

    my_df_1 = my_df.loc[my_df["Rank"] > 5, "Are you OTHER"] = "OTHER"
    my_df_1 = my_df[my_df["Are you OTHER"] == "OTHER"]
    my_df_1.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_df-FINAL_PART_2.csv",index=False)


    ## PUT THE ONES AFTER RANK=5 IN CATEGORY OTHER , replace their names with OTHER
    my_df.loc[my_df["Rank"] > 5, "Player"] = "OTHER"
    my_df = my_df.groupby(["Act","Player"],as_index=False).agg({ "Line":"sum", "PlayerLine": "sum", "PlayerPercent":"sum"})
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_dfPart2_v3.csv",index=False)

    return my_df


def clean_names(my_df):
    '''
        In the dataframe, formats the players'
        names so each word start with a capital letter.

        Returns:
            The df with formatted names
    '''
    # TODO : Clean the player names
    
    my_df["Player"] = my_df["Player"].str.capitalize()
    my_df.to_csv(r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\my_df-FINAL_PART_3.csv",index=False)
    print(my_df)    
    return my_df




if __name__ == "__main__":

    # Read data
    my_df = pd.read_csv(
        r"C:\School\INF8808E\Lab 2\DataVizLab\lab2\code\src\assets\data\romeo_and_juliet.csv"
    )

    # Run functions
    my_df = summarize_lines(my_df)
    my_df = replace_others(my_df)
    my_df = clean_names(my_df)

    # Print result
    print(my_df.head())