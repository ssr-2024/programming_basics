from io import StringIO
import contextlib
from unittest.mock import patch, MagicMock
import re
import unittest
import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
with patch('builtins.input', side_effect=['1', '0']):
    import lab.lab_103_collections as lab


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


class Test103_collections(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_summary_valid_keys(self):
        result = lab.summary([1, 2, 3, 4, 17])
        self.assertIn('max', result)
        self.assertIn('min', result)
        self.assertIn('mean', result)
        self.assertIn('sum', result)
        self.assertIn('length', result)
        self.assertIn('raw', result)

    def test_summary_valid_values(self):
        result = lab.summary([1, 2, 3, 4, 17])
        expected = {
            'max': 17,
            'min': 1,
            'mean': 5.4,
            'sum': 27,
            'length': 5,
            'raw': [1, 2, 3, 4, 17]
        }
        for key in expected:
            self.assertEqual(
                expected[key], result[key], msg=f"expected '{key}': {expected[key]}, but found {result[key]}")

    def test_print_smiley(self):
        transposed = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
                      [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
                      [0, 9, 0, 9, 0, 9, 0, 0, 9, 0],
                      [0, 9, 0, 0, 0, 9, 9, 0, 9, 0],
                      [0, 9, 0, 0, 0, 9, 9, 0, 9, 0],
                      [0, 9, 0, 9, 0, 9, 0, 0, 9, 0],
                      [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
                      [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        smiley = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
                  [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
                  [0, 9, 0, 9, 0, 0, 9, 0, 9, 0],
                  [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
                  [0, 9, 0, 9, 9, 9, 9, 0, 9, 0],
                  [0, 9, 0, 0, 9, 9, 0, 0, 9, 0],
                  [0, 9, 0, 0, 0, 0, 0, 0, 9, 0],
                  [0, 9, 9, 9, 9, 9, 9, 9, 9, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.assertEqual(smiley, lab.draw_transposed_grid(transposed))

    def test_print_grid(self):
        transposed = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
                      [9, 8, 7, 6, 5, 4, 3, 2, 1]]
        orig = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1]]
        self.assertEqual(orig, lab.draw_transposed_grid(transposed))


if __name__ == '__main__':
    unittest.main()
