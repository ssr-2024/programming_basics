import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import unittest
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


FILE_NAME = 'lab_002_variables.py'


class Test002Variables(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_exercise_1(self):
        res = script_mode.call_nth_test(FILE_NAME, '1')
        self.assertIn('name', res)
        self.assertIn('vorname', res)
        self.assertIsInstance(res['name'], str)
        self.assertIsInstance(res['vorname'], str)
        self.assertGreater(len(res['name']), 0)
        self.assertGreater(len(res['vorname']), 0)

    def test_exercise_2a(self):
        res = script_mode.call_nth_test(FILE_NAME, '2a')
        self.assertEqual(2, res['tore'])

    def test_exercise_2b(self):
        res = script_mode.call_nth_test(FILE_NAME, '2b')
        self.assertEqual(3, res['tore'])

    def test_exercise_3(self):
        with stdoutIO() as s:
            res = script_mode.call_nth_test(FILE_NAME, '3_kreisflaeche')
        self.assertIn('radius', res)
        area = pi * (res['radius']**2)
        self.assertRegex(s.getvalue(), str(area))
        

if __name__ == '__main__':
    unittest.main()
