import pandas as pd
from log_manager.log_manager import LogManager


class DateManager:
    def __init__(self):
        self.log = LogManager(log_name='DateManager')

    def timestamp_to_date(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Convert datetime columns in a dataframe to date type.

        Args:
            dataframe (pd.DataFrame): The dataframe containing the datetime columns.

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
        """
        Convert a datetime column in a dataframe to date type.

        Args:
            column (str): The name of the datetime column to convert.
            dataframe (pd.DataFrame): The dataframe containing the datetime column.

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
        except ValueError as e:
            self.log.error(e)
        return dataframe
