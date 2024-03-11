# **Custom Python Library**
Custom library for frequent used methods/libraries.

Installation : ```pip install RR-Custom-Python-Tools```

**_License_**: ```GPLv3+```

___
___


# *DateManager*

`To use the DateManager class, you need to import it and create an instance:`

```python
from date_manager.date_manager import DateManager

date_manager = DateManager()
```

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
---
---

# *LogManager*
`The LogManager class provides a customizable logging utility in Python, allowing you to log messages of different severity levels to both a file and the console.`

## **Features**
- Initialization of logging parameters such as log file name, log level, and log name.
- Logging of messages with severity levels including INFO, DEBUG, WARNING, ERROR, and CRITICAL.
- Configuration of logging to both file and console.
Customizable log message format.

`To use the LogManager class, follow these steps:`

```python
# Import the LogManager class:
from log_manager.log_manager import LogManager

# Create an instance of the LogManager class:
log_manager = LogManager()
```
`By default, this initializes the logger with the following settings:`
- Log file name: './Custom-Python_Tools.log'
- Log level: logging.DEBUG
- Log name: 'LogManager'

`Log messages with desired severity levels:`<br>
Use the appropriate methods to log messages with different severity levels:
- info(message: str)
- debug(message: str)
- warning(message: str)
- error(message: str)
- critical(message: str)

`Example:`
```python
log_manager.info("This is an informational message.")
log_manager.error("An error occurred!")
```

`Customize LogManager settings (optional):`<br>
You can customize the LogManager settings by providing parameters during initialization:

```python
log_manager = LogManager(log_file='my_log.log', log_level=logging.INFO, log_name='MyLogger')
```

 `Logging Format`

The default logging format includes the following fields:

- Timestamp (%(asctime)s)
- Logger Name (%(name)s)
- Log Level (%(levelname)s)
- Log Message (%(message)s)

You can modify the logging format by updating the formatter string in the __init__ method of the LogManager class.


---
---
- `Logging`

All of the above class utilizes a logging mechanism provided by log_manager for capturing important events during the process. Ensure you have the appropriate logger configuration to capture and manage log messages effectively.

---
- `Dependencies`
    - pandas: A powerful data manipulation library in Python used extensively for data analysis and manipulation.
    - logging: The Python standard library module used for logging functionality.

---
- `Author`
    - This module is maintained by Ronak Rathore.
