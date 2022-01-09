"""CSC110 Fall 2020 Project, Phase 2: Display

DESCRIPTION
===============================
This file contains the code responsible for displaying the results of the computations.
===============================

This file is Copyright (c) 2020 WeiZhong How and Ramy Zhang.
"""
import matplotlib.pyplot as plt
from pandas import DataFrame


def create_graph(result: DataFrame) -> None:
    """
    A function to produce a double axis graph using the DataFrame computed:
    The left y-axis would be the emissions measured in million tonnes per year
    The right y-axis would be the average temperature of the country inputted in
    The x-axis would be the time in years.

    Preconditions:
        - isinstance(result, DataFrame)
    """
    ax = result[['co2', 'methane', 'nitrous_oxide']].plot.bar(stacked=True)
    ax2 = ax.twinx()
    ax2.plot(result['year'], result['AverageTemperature'],
             color='red', label='Average Temperature (in Celsius)')
    ax.set_ylabel('Emission of Carbon Dioxide, Methane, and Nitrous Oxide (in Million Tonnes)')
    ax2.set_ylabel('Average Temperature (in Celsius)')
    ax.set_xlabel('Year')

    ax.legend(loc='upper left')
    ax2.legend(loc='lower left')

    plt.scatter(result['year'], result['AverageTemperature'], color='red', marker='.')

    plt.title('Greenhouse Gases and Their Effects on Global Land-Ocean Temperature')


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['matplotlib.pyplot', 'pandas'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
