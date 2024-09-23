import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import unittest
import sys
import contextlib
import numpy as np
from io import StringIO
try:
    from . import script_mode
except:
    import script_mode


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


FILE_NAME = 'lab_201_numpy.py'


class Test201Numpy(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_exercise_1(self):
        body = script_mode.nth_body(FILE_NAME, '1')
        self.assertNotRegex(body, "\[.*\]", msg="Array sollte nicht explizit definiert werden")
        res = script_mode.call_nth_test(FILE_NAME, '1')
        self.assertEqual(np.ndarray, type(res['array']))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], list(res['array']))

    def test_exercise_2(self):
        body = script_mode.nth_body(FILE_NAME, '2')
        self.assertNotRegex(body, "\[.*\]", msg="Array sollte nicht explizit definiert werden")
        res = script_mode.call_nth_test(FILE_NAME, '2')
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4], [4, 4, 4]])
        np.testing.assert_array_equal(expected, res['array'])

    def test_exercise_3(self):
        res = script_mode.call_nth_test(FILE_NAME, '3')
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([1, 3, 5, 7, 9])
        np.testing.assert_array_equal(expected, res['array'])

    def test_exercise_4(self):
        res = script_mode.call_nth_test(FILE_NAME, '4')
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([0, -1, 2, -1, 4, -1, 6, -1, 8, -1])
        np.testing.assert_array_equal(expected, res['array'])

    def test_exercise_5(self):
        res = script_mode.call_nth_test(FILE_NAME, '5')
        expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        if 'init' in res:
            np.testing.assert_array_equal(expected, res['init'])
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([-1, 1, -1, 3, -1, 5, -1, 7, -1, 9])
        np.testing.assert_array_equal(expected, res['array'])

    def test_exercise_reshape(self):
        res = script_mode.call_nth_test(FILE_NAME, 'reshape')
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([[0, 1, 2, 3, 4],
                             [5, 6, 7, 8, 9]])
        np.testing.assert_array_equal(expected, res['array'])

    def test_exercise_stack(self):
        res = script_mode.call_nth_test(FILE_NAME, 'stack')
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([[0, 1, 2, 3, 4],
                             [0, 0, 0, 0, 0],
                             [0, 1, 1, 0, 1],
                             [0, 1, 0, 1, 0]])
        np.testing.assert_array_equal(expected, res['array'])

    def test_exercise_range(self):
        res = script_mode.call_nth_test(FILE_NAME, 'range')
        self.assertEqual(np.ndarray, type(res['array']))
        expected = np.array([6, 9, 10])
        np.testing.assert_array_equal(expected, res['array'])


if __name__ == '__main__':
    unittest.main()
