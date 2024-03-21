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