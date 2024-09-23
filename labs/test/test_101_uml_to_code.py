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


FILE_NAME = 'lab_101_uml_to_code.py'


class Test101_UML2Code(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_output_hello_on_1(self):
        with patch('builtins.input', side_effect=['1']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, 'uml')
        self.assertEqual('Hello', s.getvalue().strip())
        
    def test_output_howdy_on_2(self):
        with patch('builtins.input', side_effect=['2']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, 'uml')
        self.assertEqual('Howdy', s.getvalue().strip())
        
    def test_output_greetings_for_rest(self):
        with patch('builtins.input', side_effect=['3']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, 'uml')
        self.assertEqual('Greetings!', s.getvalue().strip())
        with patch('builtins.input', side_effect=['99']):
            with stdoutIO() as s:
                script_mode.call_nth_test(FILE_NAME, 'uml')
        self.assertEqual('Greetings!', s.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
