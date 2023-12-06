class Date_Management:
    """
    Class containing methods to cover frequent date operations.
    """

    def __init__(self):
        """
        __init__ : constructor method.
        """
        pass

    def timestamp_to_date(dataframe):
        col_datatype_dict = dataframe.dtypes.to_dict()
        datetime_columns_list = {i for i in col_datatype_dict
                                 if col_datatype_dict[i] == 'datetime64[ns]'}
        for col in datetime_columns_list:
            dataframe[col] = dataframe[col].dt.date

        return dataframe

    def timestamp_to_date_column(dataframe, column):
        col_datatype_dict = dataframe.dtypes.to_dict()
        datetime_columns_list = {i for i in col_datatype_dict
                                 if col_datatype_dict[i] == 'datetime64[ns]'}
        for col in datetime_columns_list:
            dataframe[col] = dataframe[col].dt.date

        return dataframe
