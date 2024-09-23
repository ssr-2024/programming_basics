import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import unittest
from unittest.mock import patch
from math import pi
import sys
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


FILE_NAME = 'lab_003_errors.py'


class Test003Errors(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_exercise_1a(self):
        with self.assertRaisesRegex(TypeError, r'can only concatenate str \(not "float"\) to str'):
            script_mode.call_nth_test(FILE_NAME, '1a')

    def test_exercise_1b(self):
        with self.assertRaisesRegex(TypeError, r"^unsupported operand type\(s\) for \*\* or pow\(\): 'str' and 'int'"):
            script_mode.call_nth_test(FILE_NAME, '1b')


    def test_exercise_1c(self):
        with self.assertRaisesRegex(ZeroDivisionError, r"^division by zero"):
            script_mode.call_nth_test(FILE_NAME, '1c')


if __name__ == '__main__':
    unittest.main()
