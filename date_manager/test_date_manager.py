import pandas as pd
import unittest

from date_manager import DateManager


class TestDateManager(unittest.TestCase):

    def setUp(self) -> None:
        """
        Sets up the test fixture.

        Returns:
            None
        """
        self.df = pd.DataFrame({
            'timestamp_col_1': pd.date_range('2022-01-01', periods=5),
            'timestamp_col_2': pd.date_range('2022-02-01', periods=5),
            'other_col': [1, 2, 3, 4, 5]
        })

    def test_timestamp_to_date(self) -> None:
        """
        Test the timestamp_to_date function.

        This function takes a pandas dataframe with timestamp columns and converts them to date columns.
        It then compares the resulting dataframe with an expected dataframe.

        Parameters:
            self (unittest.TestCase): The test case object.
            df (pandas.DataFrame): The dataframe with timestamp columns.

        Returns:
            None

        """
        expected_df = pd.DataFrame({
            'timestamp_col_1': pd.date_range('2022-01-01', periods=5),
            'timestamp_col_2': pd.date_range('2022-02-01', periods=5),
            'other_col': [1, 2, 3, 4, 5]
        })
        expected_df['timestamp_col_1'] = expected_df['timestamp_col_1'].dt.date
        expected_df['timestamp_col_2'] = expected_df['timestamp_col_2'].dt.date
        result_df = DateManager.timestamp_to_date(self.df)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_timestamp_to_date_column(self) -> None:
        """
        Test the timestamp_to_date_column function.

        This function takes a single timestamp column from a pandas dataframe and converts it to a date column.
        It then compares the resulting dataframe with an expected dataframe.

        Parameters:
            self (unittest.TestCase): The test case object.
            df (pandas.DataFrame): The dataframe with the timestamp column.
            timestamp_column (str): The name of the timestamp column.

        Returns:
            pandas.DataFrame: The resulting dataframe after conversion.

        """
        expected_df = pd.DataFrame({
            'timestamp_col_1': pd.date_range('2022-01-01', periods=5),
            'timestamp_col_2': pd.date_range('2022-02-01', periods=5),
            'other_col': [1, 2, 3, 4, 5]
        })
        expected_df['timestamp_col_1'] = expected_df['timestamp_col_1'].dt.date
        result_df = DateManager.timestamp_to_date_column('timestamp_col_1', self.df)
        pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == '__main__':
    unittest.main()
