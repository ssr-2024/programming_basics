from io import StringIO
import contextlib
from math import pi
from unittest.mock import patch
import re
import unittest
import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))
with patch('builtins.input', side_effect=['1', '0']):
    from lab.lab_102_loops import triangle


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


FILE_NAME = 'lab_102_loops.py'


def sanitize(text: str):
    return re.sub('\r\n', '\n', text)


class Test102_Loops(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def test_triangle_1(self):
        with stdoutIO() as s:
            triangle(1)
        result = re.sub(' ', '', sanitize(s.getvalue())).strip()
        self.assertEqual('*', result)

    def test_triangle_2(self):
        with stdoutIO() as s:
            triangle(2)
        result = re.sub(' ', '', sanitize(s.getvalue())).strip()
        expected = re.sub(
            ' ',
            '',
            """
            *
            **
            *
            """
        ).strip()
        self.assertEqual(expected, result)

    def test_triangle_5(self):
        with stdoutIO() as s:
            triangle(5)
        result = re.sub(' ', '', sanitize(s.getvalue())).strip()
        expected = re.sub(
            ' ',
            '',
            """
            *
            **
            ***
            ****
            *****
            ****
            ***
            **
            *
            """
        ).strip()
        self.assertEqual(expected, result)

    def test_triangle_8(self):
        with stdoutIO() as s:
            triangle(8)
        result = re.sub(' ', '', sanitize(s.getvalue())).strip()
        expected = re.sub(
            ' ',
            '',
            """
            *
            **
            ***
            ****
            *****
            ******
            *******
            ********
            *******
            ******
            *****
            ****
            ***
            **
            *
            """
        ).strip()
        self.assertEqual(expected, result)

    def test_implemented_with_loop(self):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "..", "lab", FILE_NAME)
        with open(file_path, 'r+') as f:
            raw = f.read()
        self.assertRegex(raw, r'(for.*in.*:|while.*:)', 'Expecting the use of a loop inside the implementation')


if __name__ == '__main__':
    unittest.main()
