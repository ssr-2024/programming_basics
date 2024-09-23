import unittest
import os
import shutil
import sys
from pathlib import Path
import pandas as pd
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from lab.lab_303_data_analysis import *


tmp_dir = Path(os.path.join(os.path.dirname(__file__), 'tmp'))
fixture_dir = Path(os.path.join(os.path.dirname(__file__), 'fixtures'))


class Test303_data_analysis(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir(tmp_dir):
            os.mkdir(tmp_dir)

    def tearDown(self):
        if os.path.isdir(tmp_dir):
            shutil.rmtree(tmp_dir)

    def test_result(self):
        run(fixture_dir / 'suunto', export_file=tmp_dir / 'export.xlsx')
        expected = pd.read_excel(
            str(fixture_dir / 'suunto_export.xlsx'),
            index_col=0
        ).fillna(-999)
        result = pd.read_excel(
            str(tmp_dir / 'export.xlsx'),
            index_col=0
        ).fillna(-999)
        for row_name in expected.index.values:
            self.assertTrue(row_name in result.index)
            self.assertListEqual(
                expected.loc[row_name].to_list(),
                result.loc[row_name].to_list()
            )


if __name__ == '__main__':
    unittest.main()
