"""CSC110 Fall 2020 Project, Phase 2: Reading the Data

DESCRIPTION
===============================
This file contains the code responsible for reading data from data sets.
===============================

This file is Copyright (c) 2020 WeiZhong How and Ramy Zhang.
"""
import json
from typing import Dict
import pandas as pd
from pandas import DataFrame


class Csv:
    """A class that is used to read csv files.

    Representation Invariants:
        - isinstance(data, DataFrame)
    """
    data: DataFrame

    def __init__(self, file_path: str) -> None:
        """An initialization that is used to read csv file"""
        self.data = pd.read_csv(file_path)


class Json:
    """A class that is used to read json files.

        Representation Invariants:
            - len(data) > 0
            - isinstance(data, Dict)
        """
    data: Dict

    def __init__(self, file_path: str) -> None:
        """An initialization that is used to read json file"""
        with open(file_path) as json_file:
            self.data = json.load(json_file)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['json', 'pandas'],  # the names (strs) of imported modules
        'allowed-io': ['__init__'],  # the names (strs) of functions that call print/open/input
        'max-line-length': 100,
        'disable': ['R1705', 'C0200']
    })
