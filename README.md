# Custom Python Library
Custom library for frequent used methods/libraries.

Installation : ```pip install RR-Custom-Python-Tools```

**_License_**: ```GPLv3+```

___
___


## DateManager

Usage

To use the DateManager class, you need to import it and create an instance:

```python
from date_manager.date_manager import DateManager

date_manager = DateManager()
```

timestamp_to_date(dataframe: pd.DataFrame) -> pd.DataFrame

Converts datetime columns in a DataFrame to date type.

Arguments:

dataframe (pd.DataFrame): The DataFrame containing the datetime columns.
Returns:

pd.DataFrame: The input DataFrame with the datetime columns converted to date type.
Example:

python
Copy code
import pandas as pd

# Create a sample DataFrame
data = {'datetime_column': ['2022-01-01', '2022-01-02', '2022-01-03']}
df = pd.DataFrame(data)
df['datetime_column'] = pd.to_datetime(df['datetime_column'])

# Convert datetime columns to date
converted_df = date_manager.timestamp_to_date(df)
timestamp_to_date_column(column: str, dataframe: pd.DataFrame) -> pd.DataFrame
Converts a specific datetime column in a DataFrame to date type.

Arguments:

column (str): The name of the datetime column to convert.
dataframe (pd.DataFrame): The DataFrame containing the datetime column.
Returns:

pd.DataFrame: The input DataFrame with the specified datetime column converted to date type.
Raises:

ValueError: If the input DataFrame does not contain the specified datetime column.
Example:

python
Copy code
import pandas as pd

# Create a sample DataFrame
data = {'datetime_column': ['2022-01-01', '2022-01-02', '2022-01-03']}
df = pd.DataFrame(data)
df['datetime_column'] = pd.to_datetime(df['datetime_column'])

# Convert specific datetime column to date
converted_df = date_manager.timestamp_to_date_column('datetime_column', df)
Logging
The DateManager class utilizes a logging mechanism provided by log_manager for capturing important events during the conversion process. Ensure you have the appropriate logger configuration to capture and manage log messages effectively.

Dependencies
pandas: A powerful data manipulation library in Python used extensively for data analysis and manipulation.
Author
This module is maintained by [Your Name].

Feel free to contribute or report issues through GitHub [link to your GitHub repository].