import pandas as pd
import unittest

from date_manager import DateManager


class TestDateManager(unittest.TestCase):

    def setUp(self) -> None:
        self.obj_date = DateManager()
        self.df = pd.DataFrame({
            'timestamp_col_1': pd.date_range('2022-01-01', periods=5),
            'timestamp_col_2': pd.date_range('2022-02-01', periods=5),
            'other_col': [1, 2, 3, 4, 5]
        })

    def test_timestamp_to_date(self) -> None:
        expected_df = pd.DataFrame({
            'timestamp_col_1': pd.date_range('2022-01-01', periods=5),
            'timestamp_col_2': pd.date_range('2022-02-01', periods=5),
            'other_col': [1, 2, 3, 4, 5]
        })
        expected_df['timestamp_col_1'] = expected_df['timestamp_col_1'].dt.date
        expected_df['timestamp_col_2'] = expected_df['timestamp_col_2'].dt.date
        result_df = self.obj_date.timestamp_to_date(self.df)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_timestamp_to_date_column(self) -> None:
        expected_df = pd.DataFrame({
            'timestamp_col_1': pd.date_range('2022-01-01', periods=5),
            'timestamp_col_2': pd.date_range('2022-02-01', periods=5),
            'other_col': [1, 2, 3, 4, 5]
        })
        expected_df['timestamp_col_1'] = expected_df['timestamp_col_1'].dt.date
        result_df = self.obj_date.timestamp_to_date_column('timestamp_col_1', self.df)
        pd.testing.assert_frame_equal(result_df, expected_df)


if __name__ == '__main__':
    unittest.main()
