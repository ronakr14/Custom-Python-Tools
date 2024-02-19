import pandas as pd


class Date_Management:
    """
    Class containing methods to cover frequent date operations.
    """

    @staticmethod
    def timestamp_to_date(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Converts timestamp columns to date in the given DataFrame.

        Parameters:
        - dataframe (pd.DataFrame): Input DataFrame containing timestamp columns.

        Returns:
        - pd.DataFrame: DataFrame with timestamp columns converted to date.
        """
        datetime_columns = [col for col, dtype in dataframe.dtypes.items() if dtype == 'datetime64[ns]']
        dataframe[datetime_columns] = dataframe[datetime_columns].dt.date
        return dataframe

    @staticmethod
    def timestamp_to_date_column(column: str, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Converts a specific timestamp column to date in the given DataFrame.

        Parameters:
        - column (str): Name of the timestamp column to be converted.
        - dataframe (pd.DataFrame): Input DataFrame.

        Returns:
        - pd.DataFrame: DataFrame with the specified timestamp column converted to date.
        """
        dataframe[column] = dataframe[column].dt.date
        return dataframe
