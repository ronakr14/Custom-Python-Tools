from pathlib import Path
import pandas as pd
import openpyxl
from date_manager import DateManager


class ExcelManager:
    """
    Class containing methods to manage Excel files.
    """

    @staticmethod
    def get_dataframe(Workbook: str, Sheet: str) -> pd.DataFrame:
        """
        Read data from an Excel workbook and return as a DataFrame.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the sheet in the workbook.

        Returns:
        - pd.DataFrame: DataFrame containing the data from the specified sheet.
        """
        try:
            dataframe = pd.read_excel(Path(Workbook), sheet_name=Sheet)
            dataframe = DateManager.timestamp_to_date(dataframe)
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            dataframe = pd.DataFrame()
        return dataframe

    @staticmethod
    def delete_sheet(Workbook: str, Sheet: str) -> None:
        """
        Delete a sheet from an Excel workbook.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the sheet to delete.

        Returns:
        - None
        """
        wb = openpyxl.load_workbook(Workbook)
        sheet_names_list = wb.sheetnames
        sheetno = sheet_names_list.index(Sheet)
        del wb[sheet_names_list[sheetno]]
        wb.save(Workbook)

    @staticmethod
    def create_sheet(Workbook: str, Sheet: str) -> None:
        """
        Create a new sheet in an Excel workbook.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the new sheet to create.

        Returns:
        - None
        """
        wb = openpyxl.load_workbook(Workbook)
        wb.create_sheet(title=Sheet)
        wb.save(Workbook)

    @staticmethod
    def overwrite_sheet(Workbook: str, Sheet: str, dataframe: pd.DataFrame) -> None:
        """
        Overwrite data in a sheet of an Excel workbook with DataFrame content.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the sheet to overwrite.
        - dataframe (pd.DataFrame): DataFrame containing the data to write.

        Returns:
        - None
        """
        header = dataframe.columns
        Excel_Management.delete_sheet(Workbook=Workbook, Sheet=Sheet)
        Excel_Management.create_sheet(Workbook=Workbook, Sheet=Sheet)
        with pd.ExcelWriter(
            Path(Workbook), mode="a", engine="openpyxl", if_sheet_exists="overlay"
        ) as writer:
            dataframe.to_excel(
                writer, sheet_name=Sheet, header=header, startrow=0, index=False
            )

    @staticmethod
    def reposition_sheet(Workbook: str, Sheet: str) -> None:
        """
        Reposition a sheet in an Excel workbook.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the sheet to reposition.

        Returns:
        - None
        """
        wb = openpyxl.load_workbook(Workbook)
        wb.move_sheet(Sheet, -(len(wb.sheetnames) - 1))
        wb.save(Workbook)
        wb.close()

    @staticmethod
    def append_dataframe_w_password(Workbook: str, Sheet: str, Password: str, dataframe: pd.DataFrame) -> None:
        """
        Append DataFrame content to a sheet in an Excel workbook with password protection.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the sheet to append data to.
        - Password (str): Password for sheet protection.
        - dataframe (pd.DataFrame): DataFrame containing the data to append.

        Returns:
        - None
        """
        Excel_Management.remove_password_sheet(filepath=Workbook, sheetname=Sheet)
        with pd.ExcelWriter(
            Path(Workbook), mode="a", engine="openpyxl", if_sheet_exists="overlay"
        ) as writer:
            dataframe.to_excel(
                writer,
                sheet_name=Sheet,
                header=None,
                startrow=writer.sheets[Sheet].max_row,
                index=False,
            )

        Excel_Management.add_sheet_password(filepath=Workbook, sheetname=Sheet, password=Password)

    @staticmethod
    def append_dataframe_wo_password(Workbook: str, Sheet: str, dataframe: pd.DataFrame) -> None:
        """
        Append DataFrame content to a sheet in an Excel workbook without password protection.

        Parameters:
        - Workbook (str): Path to the Excel workbook file.
        - Sheet (str): Name of the sheet to append data to.
        - dataframe (pd.DataFrame): DataFrame containing the data to append.

        Returns:
        - None
        """
        with pd.ExcelWriter(
            Path(Workbook), mode="a", engine="openpyxl", if_sheet_exists="overlay"
        ) as writer:
            dataframe.to_excel(
                writer,
                sheet_name=Sheet,
                header=None,
                startrow=writer.sheets[Sheet].max_row,
                index=False,
            )

    @staticmethod
    def remove_password_sheet(filepath: str, sheetname: str) -> None:
        """
        Remove password protection from a sheet in an Excel workbook.

        Parameters:
        - filepath (str): Path to the Excel workbook file.
        - sheetname (str): Name of the sheet to remove password protection from.

        Returns:
        - None
        """
        wb = openpyxl.load_workbook(filepath)
        wb.active = wb[sheetname]
        ws = wb.active
        ws.protection
        ws.protection.sheet = False
        wb.save(filepath)
        wb.close()

    @staticmethod
    def add_sheet_password(filepath: str, sheetname: str, password: str) -> None:
        """
        Add password protection to a sheet in an Excel workbook.

        Parameters:
        - filepath (str): Path to the Excel workbook file.
        - sheetname (str): Name of the sheet to add password protection to.
        - password (str): Password for sheet protection.

        Returns:
        - None
        """
        wb = openpyxl.load_workbook(filepath)
        wb.active = wb[sheetname]
        ws = wb.active
        ws.protection
        ws.protection.sheet = True
        ws.protection.password = password
        wb.save(filepath)
        wb.close()
