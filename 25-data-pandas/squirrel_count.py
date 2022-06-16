import pandas as pd

# Reads a parses the data from a csv file
sq_data = pd.read_csv("squirrel_data_cp_2018.csv")

# counts the squirrels per Fur color values
gray_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])

squirrels_counter_by_color = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}


# creates a new dataframe from a dictionary data structure
squirrels_counter_by_color_df = pd.DataFrame(squirrels_counter_by_color)

print(squirrels_counter_by_color_df)

# dumps the data into a csv file
squirrels_counter_by_color_df.to_csv("squirrels_count.csv")
