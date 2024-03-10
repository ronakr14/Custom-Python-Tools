# Custom Python Library
Custom library for frequent used methods/libraries.

## Installation
    pip install RR-Custom-Python-Tools

## License
    GPLv3+

## DateManager

### def timestamp_to_date(dataframe: pd.DataFrame) -> pd.DataFrame:
    Static Method
    Convert datetime columns in a dataframe to date type.

    Parameters:
        dataframe (pd.DataFrame): The dataframe containing the datetime columns.

    Returns:
        pd.DataFrame: The input dataframe with the datetime columns converted to date type.

### def timestamp_to_date_column(column: str, dataframe: pd.DataFrame) -> pd.DataFrame:

    Static Method
    Convert a datetime column in a dataframe to date type.

    Parameters:
        column (str): The name of the datetime column to convert.
        dataframe (pd.DataFrame): The dataframe containing the datetime column.

    Returns:
        pd.DataFrame: The input dataframe with the datetime column converted to date type.