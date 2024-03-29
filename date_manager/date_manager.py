# date_manager/date_manager.py

"""This module allows the user to make datetime operations.

Examples:
    >>> from date_manager.date_manager import DateManager
    >>> date_manager = DateManager(log_file='abc.log')

    >>> data = {'datetime_column': ['2022-01-01', '2022-01-02', '2022-01-03']}
    >>> df = pd.DataFrame(data)
    >>> df['datetime_column'] = pd.to_datetime(df['datetime_column'])

    >>> converted_df = date_manager.timestamp_to_date(df)

    >>> converted_df = date_manager.timestamp_to_date_column('datetime_column', df)

The module contains the following methods:

- `__init__(log_file)` - creates the instance of the class.
- `timestamp_to_date(dataframe)` - returns the dataframe with all datetime column modified to date datatype.
- `timestamp_to_date_column(column, dataframe)` - returns the dataframe with specific datetime column to date datatype.
"""

import pandas as pd
from log_manager.log_manager import LogManager


class DateManager:
    def __init__(self, log_file: str = './Custom-Python_Tools.log'):
        """
        Args:
            log_file: The path to the log file.
        """
        self.log = LogManager(log_name='DateManager', log_file=log_file)
        self.log.info("DateManager initialized.")

    def timestamp_to_date(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """ Convert datetime columns in a dataframe to date type.

        Args:
            dataframe: The dataframe containing the datetime columns.

        Returns:
            pd.DataFrame: The input dataframe with the datetime columns converted to date type.
        """
        datetime_columns = [
            col for col, dtype in dataframe.dtypes.items() if dtype == 'datetime64[ns]'
        ]

        self.log.info('Datetime columns successfully fetched from dataframe.')
        self.log.info(f"Datetime columns: {datetime_columns}")

        for col in datetime_columns:
            dataframe[col] = dataframe[col].dt.date
            self.log.info(f"Datetime column:{col} converted.")

        return dataframe

    def timestamp_to_date_column(self, column: str, dataframe: pd.DataFrame) -> pd.DataFrame:
        """Convert a datetime column in a dataframe to date type.

        Args:
            column: The name of the datetime column to convert.
            dataframe: The dataframe containing the datetime column.

        Returns:
            pd.DataFrame: The input dataframe with the datetime column converted to date type.

        Raises:
            ValueError: If the input dataframe does not contain the specified datetime column.
        """
        try:
            if column not in dataframe.columns:
                raise ValueError(
                    f"The input dataframe does not contain the specified datetime column: {column}"
                )
            dataframe[column] = dataframe[column].dt.date
            self.log.info(f"Datetime column:{column} converted.")
        except ValueError as e:
            self.log.error(e)
        return dataframe
