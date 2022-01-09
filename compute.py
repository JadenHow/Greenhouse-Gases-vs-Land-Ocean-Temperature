"""CSC110 Fall 2020 Project, Phase 2: Computations

DESCRIPTION
===============================
This file contains the code responsible for computing the data.
===============================

This file is Copyright (c) 2020 WeiZhong How and Ramy Zhang.
"""
from typing import List, Dict
from pandas import DataFrame
from read import Csv, Json


def average_temperature_per_year(csv: Csv, country: str) -> DataFrame:
    """A function to calculate the average temperature of a country inputted.

    Preconditions:
        - len(country) > 0
        - isinstance(csv, Csv)
        - country in csv.data['Country'].values
    """
    filtered_data = csv.data.loc[(csv.data['dt'] >= '1990-01-01')
                                 & (csv.data['Country'] == country)]
    average_temp = filtered_data['dt'].str.slice(stop=4).to_frame()\
        .join(filtered_data['AverageTemperature']).groupby('dt').mean()
    year = filtered_data['dt'].str.slice(stop=4).unique()
    average_temp['year'] = year
    return average_temp


def filter_empty_data(json: Json, country: str) -> List:
    """A function to filter out the empty data from the json file.

    Preconditions:
        - isinstance(json, Json)
        - len(country) > 0
        - country in json.data
    """
    return [yearly_data for yearly_data in json.data[country]['data']
            if yearly_data.get('co2', 0) != 0 and yearly_data.get('methane', 0) != 0
            and yearly_data.get('nitrous_oxide', 0) != 0]


def select_column(lst: List, variable: str, year: int) -> List:
    """A function to select any column of data in the json file until the year inputted.

    Preconditions:
        - isinstance(lst, list)
        - len(variable) > 0
        - all([variable in lst[i] for i in range(0, len(lst))])
        - 1990 <= year <= 2018
    """
    return [x[variable] for x in lst if int(x.get('year')) <= year]


def percentages(country: str, file_name: str) -> Dict[str, List[float]]:
    """A function to calculate the percentages of CO2, CH4, and N2O emissions
    relative to each other. These percentages will be used for the pie chart
    animation of emissions over the years.

    Preconditions:
        - country in Json(file_name).data
        - len(country) > 0
    """
    # utilizing functions from the compute module to access the emissions data
    json_data = Json(file_name)
    data = filter_empty_data(json_data, country)
    # creating "accumulator" variables that will later be populated by data
    gas_emissions = {'co2': [], 'methane': [], 'nitrous_oxide': []}
    gas_totals = [0] * 25

    for gas in gas_emissions:
        gas_emissions[gas] = select_column(data, gas, 2013)
        for i in range(0, 24):
            gas_totals[i] += gas_emissions[gas][i]

    for i in range(0, 24):
        for gas in gas_emissions:
            gas_emissions[gas][i] = (gas_emissions[gas][i] / gas_totals[i]) * 100

    return gas_emissions


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['read', 'pandas'],  # the names (strs) of imported modules
        'allowed-io': [],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
