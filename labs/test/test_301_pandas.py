import unittest
import os
import shutil
import sys
import pandas as pd
import numpy as np
from pathlib import Path

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from lab.lab_301_pandas import *

tmp_dir = Path(os.path.join(os.path.dirname(__file__), 'tmp'))
fixture_dir = Path(os.path.join(os.path.dirname(__file__), 'fixtures'))


class Test301_pandas(unittest.TestCase):
    def setUp(self):
        if not tmp_dir.is_dir():
            tmp_dir.mkdir()

    def tearDown(self):
        if tmp_dir.is_dir():
            shutil.rmtree(tmp_dir)

    def test_1_experiment_setup(self):
        xlsx = tmp_dir / 'exp_setup.xlsx'
        experiment_setup(xlsx)
        result = pd.read_excel(
            xlsx,
            index_col=0
        )
        expected = {
            'vpn01': {
                'Gruppe': 'A',
                'Trial_01': 'vid_01.mp4',
                'Trial_02': 'vid_02.mp4',
                'Trial_03': 'vid_03.mp4',
                'Trial_04': 'vid_04.mp4'
            },
            'vpn02': {
                'Gruppe': 'B',
                'Trial_01': 'vid_03.mp4',
                'Trial_02': 'vid_04.mp4',
                'Trial_03': 'vid_01.mp4',
                'Trial_04': 'vid_02.mp4'
            }
        }
        self.assertDictEqual(expected, result.transpose().to_dict())

    def test_2a_load_returns_4columns(self):
        csv = fixture_dir / 'test301_data.csv'
        result = load_relevant_data(csv)
        self.assertListEqual(
            ['country', 'height', 'weight', 'sport'],
            list(result.columns.values)
        )

    def test_2b_load_returns_12_rows(self):
        csv = fixture_dir / 'test301_data.csv'
        result = load_relevant_data(csv)
        self.assertEqual(
            12,
            result.index.size
        )

    def test_2c_load_removes_UNKNOWN_values(self):
        csv = fixture_dir / 'test301_data.csv'
        result = load_relevant_data(csv)
        self.assertEqual(0, (result == np.nan).sum().sum())
        self.assertEqual(0, (result == 'UNKNOWN').sum().sum())

    def test_2d_load_contains_sport_in_last_column(self):
        csv = fixture_dir / 'test301_data.csv'
        result = load_relevant_data(csv)
        self.assertListEqual(
            ['Basketball', 'Volleyball'],
            sorted(result['sport'].unique())
        )


if __name__ == '__main__':
    unittest.main()
