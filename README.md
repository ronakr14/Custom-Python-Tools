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
date_manager = DateManager(log_file='abc.log')
```
- Arguments:
    - log_file (str): log_file path. Defaults to './Custom-Python_Tools.log'. Custom path can be provided.

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
# *ExcelManager*
`To use the ExcelManager class, you need to import it and create an instance:`

```python
from excel_manager.excel_manager import ExcelManager
excel_manager = ExcelManager(log_file='abc.log')
```
- Arguments:
    - log_file (str): log_file path. Defaults to './Custom-Python_Tools.log'
### `get_dataframe(self, workbook: str, sheet: str) -> pd.DataFrame`
Retrieve a pandas dataframe from an Excel workbook.
- Args:
    - workbook (str): The path to the Excel workbook.
    - sheet (str): The name of the sheet containing the data.
- Returns:
    - pd.DataFrame: The contents of the specified sheet as a pandas dataframe.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - Exception: If an unexpected error occurs.

`Example:`
```python
workbook = "test.xlsx"
sheet = "Sheet1"
dataframe = excel_manager.get_dataframe(workbook, sheet)
```
### `delete_sheet(self, workbook: str, sheet: str) -> None`
Delete a sheet from an Excel workbook.<br>
! There should be minimum 2 sheets in the workbook to perform this operation.

- Args:
    - workbook (str): The path to the Excel workbook.
    - sheet (str): The name of the sheet to be deleted.
- Returns:
    - None: Returns nothing.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - ValueError: If the specified sheet does not exist in the workbook.
    - Exception: If an unexpected error occurs.

`Example:`
```python
workbook = "test.xlsx"
sheet = "Sheet1"
excel_manager.delete_sheet(workbook, sheet)
```
### `create_sheet(self, workbook: str, sheet: str) -> None`
Create a new sheet in an Excel workbook.
- Args:
    - workbook (str): The path to the Excel workbook.
    - sheet (str): The name of the sheet to be created.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - PermissionError: If the user does not have permission to write to the specified workbook.
    - Exception: If an unexpected error occurs.
- Returns:
    - None: Returns nothing.

`Example:`
```python
workbook = "test.xlsx"
sheet = "Sheet1"
excel_manager.create_sheet(workbook, sheet)
```
### `overwrite_sheet(self, workbook: str, sheet: str, dataframe: pd.DataFrame) -> None`
Overwrite the contents of an Excel sheet with a new dataframe.
- Args:
    - workbook (str): The path to the Excel workbook.
    - sheet (str): The name of the sheet to be overwritten.
    - dataframe (pd.DataFrame): The new contents of the sheet as a pandas dataframe.
- Returns:
    - None: Returns nothing.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - PermissionError: If the user does not have permission to write to the specified workbook.
    - ValueError: If the specified sheet does not exist in the workbook.
    - Exception: If an unexpected error occurs.

`Example:`
```python
import pandas as pd

workbook = "test.xlsx"
sheet = "Sheet1"
dataframe = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
excel_manager.overwrite_sheet(workbook, sheet, dataframe)     
```
### `reposition_sheet(self, workbook: str, sheet: str) -> None`
Moves a sheet at the start in the workbook and saves the changes.
- Args:
    - workbook (str): The path to the Excel workbook.
    - sheet (str): The name of the sheet to be moved.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - PermissionError: If the user does not have permission to write to the specified workbook.
    - ValueError: If the specified sheet does not exist in the workbook.
    - Exception: If an unexpected error occurs.
- Returns:
    - None: Returns nothing.

`Example:`
```python
workbook = "test.xlsx"
sheet = "Sheet1"
excel_manager.reposition_sheet(workbook, sheet)
```
### `append_dataframe(self, workbook: str, sheet: str, dataframe: pd.DataFrame, password: str = None) -> None`
Appends a pandas dataframe to an Excel sheet.
- Args:
    - workbook (str): The path to the Excel workbook.
    - sheet (str): The name of the sheet to which the dataframe will be appended.
    - dataframe (pd.DataFrame): The pandas dataframe to be appended to the sheet.
    - password (str, optional): The password for the Excel workbook, if it is protected. Defaults to None.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - PermissionError: If the user does not have permission to write to the specified workbook.
    - Exception: If an unexpected error occurs.
- Returns:
    - None: Returns nothing.

`Example:`
```python
import pandas as pd

workbook = "test.xlsx"
sheet = "Sheet1"
dataframe = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
excel_manager.append_dataframe(workbook, sheet, dataframe)
```
### `modify_sheet_protection(self, filepath: str, sheetname: str, enable_protection: bool, password: str = None) -> None`
Modifies the protection of an Excel sheet.
- Args:
    - filepath (str): The path to the Excel workbook.
    - sheetname (str): The name of the sheet to be protected.
    - enable_protection (bool): A boolean value indicating whether to enable or disable protection.
    - password (str, optional): The password for the Excel workbook, if it is protected. Defaults to None.
- Raises:
    - FileNotFoundError: If the specified workbook cannot be found.
    - PermissionError: If the user does not have permission to write to the specified workbook.
- Returns:
    - None: Returns nothing.

`Example:`
```python
# to set the protection, 'abc' is password.
workbook = "test.xlsx"
sheet = "Sheet1"
excel_manager.modify_sheet_protection(workbook, sheet, True, 'abc')

# to remove the protection.
workbook = "test.xlsx"
sheet = "Sheet1"
excel_manager.modify_sheet_protection(workbook, sheet, False)
```
---
---
# *MailManager*
`To use the MailManager class, you need to import it and create an instance:`

```python
from mail_manager.mail_manager import MailManager
mail_manager = MailManager(subject='abc', receiver ='abc@xyz.com', body='abc', log_file='abc.log')
```
- Args:
    - subject (str): The subject of the email.
    - receiver (Union[list, str]): A list of email addresses or a single email address.
    - body (str): The body of the email.
    - service (str, optional): The service to be used for sending the email. Defaults to 'windows'. Options-windows/smtp
    - log_file (str, optional): The path of the log file. Defaults to './Custom-Python_Tools.log'.

### `send_mail( self, copy_receiver: Union[list, str, None], attachment: Union[list, str, None], sender: str = None, sender_credentials: str = None,) -> bool:`
```python
receiver = ['abc@xyx.com', 'mnp@xyx.com']
attachment = ['abc.txt', 'mnp.xlsx']
sender = "abc@mnp.com"
sender_credentials = "abcd1234"

result = mail_manager.send_mail(sender=sender, sender_credentials=sender_credentials, copy_receiver=copy_receiver, attachment=attachment)
```
This function sends an email using the selected service.
- Args:
    - copy_receiver (Union[list, str, None]): A list of email addresses or a single email address to be added as a carbon copy (CC) of the email.
    - attachment (Union[list, str, None]): A list of email addresses or a single email address to be attached to the email.
    - sender (str, optional): The email address of the sender. If not specified, the default sender set in the system will be used.
    - sender_credentials (str, optional): The password or API key of the sender. If not specified, the default credentials set in the system will be used.
- Returns:
    - bool: A boolean value indicating whether the email was sent successfully or not.
- Raises:
    - ValueError: If the selected service is not supported.


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
### `Logging`<br>
All of the above class utilizes a logging mechanism provided by log_manager for capturing important events during the process. Ensure you have the appropriate logger configuration to capture and manage log messages effectively.

---
### `Dependencies`
- pandas: A powerful data manipulation library in Python used extensively for data analysis and manipulation.
- logging: The Python standard library module used for logging functionality.
- openpyxl: A Python library to read/write Excel 2010 xlsx/xlsm files
- inspect: The inspect module helps in checking the objects present in the code that we have written.

---
### `Author`
- This module is maintained by Ronak Rathore.
