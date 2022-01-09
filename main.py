"""CSC110 Fall 2020 Project, Phase 2: Main Script

DESCRIPTION
===============================
This file consists of the code necessary to run your entire program from start to
finish, creating the double axis graphs and the pie chart animation.
===============================

This file is Copyright (c) 2020 WeiZhong How and Ramy Zhang.
"""
# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
from read import Csv, Json
import compute
import display


# In the Python console, type in the function create_double_axis()
# and insert any country you are interested in.
# It will then show the double-axis graph. Click expand to get a better view of the graph.
def create_double_axis(country: str) -> None:
    """
    A function to produce a double axis graph:
    The left y-axis would be the emissions measured in million tonnes per year
    The right y-axis would be the average temperature of the country inputted in
    The x-axis would be the time in years.

    Preconditions:
        - country in Json(json_file_name).data
    """
    csv_data = Csv('datasets/GlobalLandTemperaturesByCountry.csv')
    json_data = Json('datasets/owid-co2-data.json')

    frame = compute.average_temperature_per_year(csv_data, country)
    data = compute.filter_empty_data(json_data, country)
    frame['co2'] = compute.select_column(data, 'co2', 2013)
    frame['methane'] = compute.select_column(data, 'methane', 2013)
    frame['nitrous_oxide'] = compute.select_column(data, 'nitrous_oxide', 2013)

    display.create_graph(frame)


# Uncomment the following lines to look at the animated pie chart. (Line 41 - 76) & (Line 11 & 12)
# # Necessary variables for pie chart animation
# COLORS = ['gold', 'red', 'magenta']
# EXPLODE = (0.01, 0.01, 0.01)
# LABELS = ['CO2', 'CH4', 'N2O']
#
# CN_PERCENTS = compute.percentages('China', 'datasets/owid-co2-data.json')
# US_PERCENTS = compute.percentages('United States', 'datasets/owid-co2-data.json')
#
# FIG, (AX1, AX2) = plt.subplots(2, 1)
#
#
# # helper function that "redraws" the figure at each frame
# def update(i: int) -> None:
#     """
#     A helper function that is called repeatedly during the loop in the
#     FuncAnimation method in order to draw the pie chart at each new animation frame.
#     """
#     AX1.clear()
#     AX2.clear()
#     AX1.axis('equal')
#     AX2.axis('equal')
#
#     cn_array = [CN_PERCENTS['co2'][i], CN_PERCENTS['methane'][i], CN_PERCENTS['nitrous_oxide'][i]]
#     AX1.pie(cn_array, explode=EXPLODE, labels=LABELS, colors=COLORS,
#             autopct='%1.1f%%', shadow=True, startangle=140)
#     AX1.set_title("China: " + str(1990 + i))
#
#     us_array = [US_PERCENTS['co2'][i], US_PERCENTS['methane'][i], US_PERCENTS['nitrous_oxide'][i]]
#     AX2.pie(us_array, explode=EXPLODE, labels=LABELS, colors=COLORS,
#             autopct='%1.1f%%', shadow=True, startangle=140)
#     AX2.set_title("United States: " + str(1990 + i))
#
#
# # display the pie chart animation!
# ANIMATOR = animation.FuncAnimation(FIG, update, frames=range(24), repeat=True, interval=50)
# plt.show()


# if __name__ == '__main__':
#     import python_ta
#
#     python_ta.check_all(config={
#         'extra-imports': ['read', 'compute', 'display', 'matplotlib.pyplot',
#                           'matplotlib.animation',
#                           'percentages'],  # the names (strs) of imported modules
#         'allowed-io': [],  # the names (strs) of functions that call print/open/input
#         'max-line-length': 100,
#         'disable': ['R1705', 'C0200']
#     })
