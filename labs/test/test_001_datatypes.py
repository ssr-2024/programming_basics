import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import unittest
from unittest.mock import patch
import time
import contextlib
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


FILE_NAME = 'lab_001_datatypes.py'


class Test001Datatypes(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_exercise_1(self):
        res = script_mode.call_nth_test(FILE_NAME, '1')
        self.assertEqual('Yes' + 'YesYes', res['exercise1_a'])
        self.assertEqual('NoNoNo' * 3, res['exercise1_b'])
        self.assertEqual('12 * 3 = {12 * 3}', res['exercise1_c'])
        self.assertEqual(f'12 * 3 = {12 * 3}', res['exercise1_d'])

    def test_exercise_2a(self):
        with stdoutIO() as s:
            script_mode.call_nth_test(FILE_NAME, '2a')
        self.assertEqual('I have scored 3 goals.', s.getvalue().strip())

    def test_exercise_2b(self):
        with patch('builtins.input', side_effect=['1.8', '75.2']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '2b')
        self.assertEqual('My BMI is 23.209876543209877.', s.getvalue().strip())

    def test_exercise_2c(self):
        with patch('builtins.input', side_effect=['Hello ', '5']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '2c')
        self.assertEqual('Hello Hello Hello Hello Hello', s.getvalue().strip())

    def test_exercise_2d(self):
        time.sleep(1)
        with patch('builtins.input', side_effect=['15']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '2d')
        self.assertEqual('15 times 3 = 45', s.getvalue().strip())

    def test_exercise_3a(self):
        with patch('builtins.input', side_effect=['Hello']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '3a')
        self.assertEqual('5 Letters', s.getvalue().strip())
        with patch('builtins.input', side_effect=['My length is 16.']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '3a')
        self.assertEqual('16 Letters', s.getvalue().strip())

    def test_exercise_3b(self):
        time.sleep(1)
        with patch('builtins.input', side_effect=['Hello']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '3b')
        res = s.getvalue().strip()
        self.assertRegex(res, "^Hello.*5*Letters")
        with patch('builtins.input', side_effect=['My length is 16.']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, '3b')
        res = s.getvalue().strip()
        self.assertRegex(res, "My length is 16.: 16 Letters")


if __name__ == '__main__':
    unittest.main()
