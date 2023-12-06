# Custom Python Library

Custom library for frequent used methods/libraries.

## Installation

    pip install RR-Custom-Python-Library

## Datetime Conversions

### timestamp_to_date(dataframe)

&emsp;&emsp;*Method converts all datetime column to date datatype.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**dataframe: A dataframe which needs datetime operation.**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**dataframe: Converted dataframe after datetime to date operation.**
<br>

### timestamp_to_date_column(column : str, dataframe)

&emsp;&emsp;*Method converts datetime column to date datatype.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**dataframe: A dataframe which needs datetime operation.**
<br>
&emsp;&emsp;&emsp;&emsp;**column: A column name which needs datetime operation.**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**dataframe: Converted dataframe after datetime to date operation.**
<br>

## Excel Operations

*Default Engine : Openpyxl*

### get_dataframe(Workbook: str, Sheet: str)

&emsp;&emsp;*Method loads excel sheet data into panda dataframe.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**dataframe: dataframe from data extracted from sheet in workbook.**
<br>

### append_dataframe_wo_password(Workbook: str, Sheet: str, dataframe)

&emsp;&emsp;*Method to append dataframe data to unprotected excel sheet.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;&emsp;&emsp;**datframe: Dataframe to append**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### delete_sheet(Workbook: str, Sheet: str)

&emsp;&emsp;*Method to delete excel sheet from workbook.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### create_sheet(Workbook: str, Sheet: str)

&emsp;&emsp;*Method to create sheet in excel workbook.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### overwrite_sheet(Workbook: str, Sheet: str, dataframe)

&emsp;&emsp;*Method to overwrite excel sheet contents.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;&emsp;&emsp;**datframe: Dataframe to overwrite**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### reposition_sheet(Workbook: str, Sheet: str)

&emsp;&emsp;*Method to reposition excel sheet to first position.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### append_dataframe_w_password(Workbook: str, Sheet: str, Password: str, df)

&emsp;&emsp;*Method to append dataframe to password protected excel sheet.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;&emsp;&emsp;**Password: Sheet password**
<br>
&emsp;&emsp;&emsp;&emsp;**datframe: Dataframe to overwrite**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### remove_password_sheet(Workbook: str, Sheet: str)

&emsp;&emsp;*Method to remove password from protected sheet.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>

### add_sheet_password(Workbook: str, Sheet: str, Password: str)

&emsp;&emsp;*Method to create password protected sheet.*
<br>
&emsp;&emsp;*input :*
<br>
&emsp;&emsp;&emsp;&emsp;**Workbook: Excel workbook path + filename.**
<br>
&emsp;&emsp;&emsp;&emsp;**Sheet: Excel workbook sheet name**
<br>
&emsp;&emsp;&emsp;&emsp;**Password: Sheet password**
<br>
&emsp;&emsp;*returns:*
<br>
&emsp;&emsp;&emsp;&emsp;**None**
<br>