import pandas as pd


class DateManager:

    @staticmethod
    def timestamp_to_date(dataframe: pd.DataFrame) -> pd.DataFrame:
        """
            Convert datetime columns in a dataframe to date type.

            Parameters:
            dataframe (pd.DataFrame): The dataframe containing the datetime columns.

            Returns:
            pd.DataFrame: The input dataframe with the datetime columns converted to date type.
        """
        datetime_columns = [col for col, dtype in dataframe.dtypes.items() if dtype == 'datetime64[ns]']
        # DateManager.log.info('Datetime columns successfully fetched from dataframe.')
        # DateManager.log.info(f"Datetime columns: {datetime_columns}")
        for col in datetime_columns:
            dataframe[col] = dataframe[col].dt.date
            # DateManager.log.info(f"Datetime column:{col} converted.")

        return dataframe

    @staticmethod
    def timestamp_to_date_column(column: str, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Convert a datetime column in a dataframe to date type.

        Parameters:
        column (str): The name of the datetime column to convert.
        dataframe (pd.DataFrame): The dataframe containing the datetime column.

        Returns:
        pd.DataFrame: The input dataframe with the datetime column converted to date type.
        """
        dataframe[column] = dataframe[column].dt.date
        return dataframe
