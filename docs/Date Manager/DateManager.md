# *DateManager*

`To use the DateManager class, you need to import it and create an instance:`

```python
from date_manager.date_manager import DateManager

date_manager = DateManager(log_file='abc.log')
```
- Arguments:
    - log_file (str): log_file path. Defaults to './Custom-Python_Tools.log'
### `timestamp_to_date(dataframe: pd.DataFrame) -> pd.DataFrame`
Converts datetime columns in a DataFrame to date type.

- Arguments:
    - dataframe (pd.DataFrame): The DataFrame containing the datetime columns.
- Returns:
    - pd.DataFrame: The input DataFrame with the datetime columns converted to date type.

`Example:`
```python
import pandas as pd

# Create a sample DataFrame
data = {'datetime_column': ['2022-01-01', '2022-01-02', '2022-01-03']}
df = pd.DataFrame(data)
df['datetime_column'] = pd.to_datetime(df['datetime_column'])

# Convert datetime columns to date
converted_df = date_manager.timestamp_to_date(df)
```

### `timestamp_to_date_column(column: str, dataframe: pd.DataFrame) -> pd.DataFrame`
Converts a specific datetime column in a DataFrame to date type.

- Arguments:
    - column (str): The name of the datetime column to convert.
    - dataframe (pd.DataFrame): The DataFrame containing the datetime column.
- Returns:
    - pd.DataFrame: The input DataFrame with the specified datetime column converted to date type.
- Raises:
    - ValueError: If the input DataFrame does not contain the specified datetime column.

`Example:`
```python
import pandas as pd

# Create a sample DataFrame
data = {'datetime_column': ['2022-01-01', '2022-01-02', '2022-01-03']}
df = pd.DataFrame(data)
df['datetime_column'] = pd.to_datetime(df['datetime_column'])

# Convert specific datetime column to date
converted_df = date_manager.timestamp_to_date_column('datetime_column', df)
```