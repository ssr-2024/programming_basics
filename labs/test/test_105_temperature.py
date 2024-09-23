import contextlib
from io import StringIO
import importlib
from unittest.mock import patch
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# import will run the script immediately. We have to
# provide inputs here...
with patch('builtins.input', side_effect=['1', '0']):
    from lab.lab_105_temperature import *


@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


class Test105_temperature(unittest.TestCase):
    def test_1_celsius_to_kelvin(self):
        self.assertEqual(0, celsius_to_kelvin(-273.15))
        self.assertEqual(273.15, celsius_to_kelvin(0))
        self.assertEqual(300, celsius_to_kelvin(26.85))

    def test_2_kelvin_to_celsius(self):
        self.assertEqual(-273.15, kelvin_to_celsius(0))
        self.assertEqual(0, kelvin_to_celsius(273.15))
        self.assertAlmostEqual(26.85, kelvin_to_celsius(300))

    def test_3_celsius_to_fahrenheit(self):
        self.assertEqual(32, celsius_to_fahrenheit(0))
        self.assertAlmostEqual(0, celsius_to_fahrenheit(-17.7777), 3)

    def test_4_fahrenheit_to_celsius(self):
        self.assertEqual(0, fahrenheit_to_celsius(32))
        self.assertAlmostEqual(-17.7777, fahrenheit_to_celsius(0), 3)

    def test_5_unit_input(self):
        self.assertEqual('Celsius', unit_input(1))
        self.assertEqual('Celsius', unit_input(2))
        self.assertEqual('Kelvin', unit_input(3))
        self.assertEqual('Kelvin', unit_input(4))
        self.assertEqual('Fahrenheit', unit_input(5))
        self.assertEqual('Fahrenheit', unit_input(6))

    def test_6_unit_output(self):
        self.assertEqual('Celsius', unit_output(3))
        self.assertEqual('Celsius', unit_output(5))
        self.assertEqual('Kelvin', unit_output(1))
        self.assertEqual('Kelvin', unit_output(6))
        self.assertEqual('Fahrenheit', unit_output(2))
        self.assertEqual('Fahrenheit', unit_output(4))

    def test_7_transform_30celsius_to_kelvin(self):
        with patch('builtins.input', side_effect=['1', '30']):
            with stdoutIO() as s:
                importlib.reload(sys.modules['lab.lab_105_temperature'])
        out = s.getvalue().strip()

        self.assertRegex(out, '30.00?\D.*Celsius.*303.15\D.*Kelvin')

    def test_8_transform_30celsius_to_fahrenheit(self):
        with patch('builtins.input', side_effect=['2', '30']):
            with stdoutIO() as s:
                importlib.reload(sys.modules['lab.lab_105_temperature'])
        out = s.getvalue().strip()
        self.assertRegex(out, '30.00?\D.*Celsius.*86.0\D.*Fahrenheit')

    def test_9_transform_10Kelvin_to_celsius(self):
        with patch('builtins.input', side_effect=['3', '10']):
            with stdoutIO() as s:
                importlib.reload(sys.modules['lab.lab_105_temperature'])
        out = s.getvalue().strip()
        self.assertRegex(out, '10.00?\D.*Kelvin.*-263.15\D.*Celsius')

    def test_11_transform_10kelvin_to_fahrenheit(self):
        with patch('builtins.input', side_effect=['4', '10']):
            with stdoutIO() as s:
                importlib.reload(sys.modules['lab.lab_105_temperature'])
        out = s.getvalue().strip()
        self.assertRegex(out, '10.00?\D.*Kelvin.*-441.6699.*Fahrenheit')

    def test_12_transform_77fahrenheit_to_celsius(self):
        with patch('builtins.input', side_effect=['5', '77']):
            with stdoutIO() as s:
                importlib.reload(sys.modules['lab.lab_105_temperature'])
        out = s.getvalue().strip()
        self.assertRegex(out, '77.00?\D.*Fahrenheit.*25.0\D.*Celsius')

    def test_13_transform_75fahrenheit_to_kelvin(self):
        with patch('builtins.input', side_effect=['6', '75']):
            with stdoutIO() as s:
                importlib.reload(sys.modules['lab.lab_105_temperature'])
        out = s.getvalue().strip()
        self.assertRegex(out, '75.00?\D.*Fahrenheit.*297.0388.*Kelvin')


if __name__ == '__main__':
    unittest.main()
