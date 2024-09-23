from io import StringIO
import contextlib
from math import pi
from unittest.mock import patch
import re
import unittest
import pytest
import os
from pathlib import Path
import shutil
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
from lab.lab_302_pathlib import *


tmp_dir = Path(os.path.join(os.path.dirname(__file__), 'tmp_dir'))
exp1_dir = tmp_dir.joinpath('experiment_01')
exp2_dir = tmp_dir.joinpath('experiment_02')


class Test302_pathlib(unittest.TestCase):

    def setUp(self):
        if tmp_dir.is_dir():
            shutil.rmtree(tmp_dir)
        tmp_dir.mkdir()
        exp1_dir.mkdir()
        exp1_dir.joinpath(f'readme.md').touch()
        for vpn in range(0, 20):
            exp1_dir.joinpath(f'vp_{vpn}.csv').touch()

        exp2_dir = tmp_dir.joinpath('experiment_02')
        exp2_dir.mkdir()
        exp2_dir.joinpath(f'readme.md').touch()
        for vpn in range(0, 15):
            vp_dir = exp2_dir.joinpath(f'vp_{vpn}')
            vp_dir.mkdir()
            for mzp in range(0, 7):
                vp_dir.joinpath(f't_0{mzp}.csv').touch()

    def tearDown(self):
        if tmp_dir.exists():
            shutil.rmtree(tmp_dir)

    def test_exp01a_returns_dict(self):
        exp01 = vpns_exp01(str(exp1_dir))
        self.assertIsInstance(exp01, dict)

    def test_exp01b_returns_names_as_keys(self):
        exp01 = vpns_exp01(str(exp1_dir))
        self.assertListEqual(
            [
                'vp_0', 'vp_1', 'vp_10', 'vp_11', 'vp_12', 'vp_13', 'vp_14', 'vp_15', 'vp_16', 'vp_17', 'vp_18', 'vp_19', 'vp_2', 'vp_3', 'vp_4', 'vp_5', 'vp_6', 'vp_7', 'vp_8', 'vp_9'
            ],
            sorted(exp01.keys())
        )

    def test_exp01c_returns_path_objects(self):
        exp01 = vpns_exp01(str(exp1_dir))
        for file_path in exp01.values():
            self.assertIsInstance(file_path, Path)

    def test_exp01d_returns_only_csv(self):
        exp01 = vpns_exp01(str(exp1_dir))
        for file_path in exp01.values():
            self.assertEqual('.csv', file_path.suffix)

    def test_exp01e_returns_correct_path(self):
        exp01 = vpns_exp01(str(exp1_dir))
        for vpn, folder in exp01.items():
            self.assertEqual(
                exp1_dir.joinpath(f'{vpn}.csv').resolve(),
                folder.resolve()
            )

    def test_exp02a_returns_dict(self):
        exp02 = vpns_exp02(str(exp2_dir))
        self.assertIsInstance(exp02, dict)

    def test_exp02b_returns_names_as_keys(self):
        exp02 = vpns_exp02(str(exp2_dir))
        self.assertListEqual(
            [
                'vp_0', 'vp_1', 'vp_10', 'vp_11', 'vp_12', 'vp_13', 'vp_14', 'vp_2', 'vp_3', 'vp_4', 'vp_5', 'vp_6', 'vp_7', 'vp_8', 'vp_9'
            ],
            sorted(exp02.keys())
        )

    def test_exp02c_returns_dicts(self):
        exp02 = vpns_exp02(str(exp2_dir))
        for mzps in exp02.values():
            self.assertIsInstance(mzps, dict)

    def test_exp02d_mzps_have_numeric_keys(self):
        exp02 = vpns_exp02(str(exp1_dir))
        for mzps in exp02.values():
            for mzp in mzps.keys():
                self.assertIsInstance(mzp, int)

    def test_exp02e_returns_correct_paths(self):
        exp02 = vpns_exp02(str(exp1_dir))
        for vpn, mzps in exp02.items():
            for mzp, file_path in mzps.items():
                self.assertEqual(
                    exp2_dir.joinpath(vpn, f'mzp_{mzp}.csv').resolve(),
                    file_path.resolve()
                )


if __name__ == '__main__':
    unittest.main()
