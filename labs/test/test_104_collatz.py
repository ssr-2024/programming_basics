import contextlib
from io import StringIO
from unittest.mock import patch
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
with patch('builtins.input', side_effect=['1', '0']):
    from lab.lab_104_collatz import collatz, run


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


class Test104_Collatz(unittest.TestCase):
    def test_1_expect_3n_and_1_for_uneven(self):
        self.assertEqual(4, collatz(1))
        self.assertEqual(28, collatz(9))
        self.assertEqual(100, collatz(33))

    def test_2_expect_half_n_for_even(self):
        self.assertEqual(1, collatz(2))
        self.assertEqual(25, collatz(50))
        self.assertEqual(50, collatz(100))

    def test_3_run_prints_numbers(self):
        with patch('builtins.input', side_effect=['5']):
            with stdoutIO() as s:
                run()
        out = s.getvalue()
        self.assertRegex(out, '5\.?0?.*\s*16\.?0?.*\s*8\.?0?.*\s*4\.?0?.*\s*2\.?0?.*\s*1\.?0?\D*',
                         msg=f'{out} expected to include the numbers "5, 16, 8, 4, 2, 1"')

    def test_4_run_returns_numbers(self):
        numbers = []
        with patch('builtins.input', side_effect=['5']):
            numbers = run()
        self.assertEqual([5, 16, 8, 4, 2, 1], numbers[0:6])

    def test_5_collatz_stops_after_421421421(self):
        numbers = []
        with patch('builtins.input', side_effect=['5']):
            numbers = run()
        self.assertEqual([5, 16, 8, 4, 2, 1, 4, 2, 1, 4, 2, 1], numbers)


if __name__ == '__main__':
    unittest.main()
