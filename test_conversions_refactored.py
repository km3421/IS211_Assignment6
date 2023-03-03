import unittest
from conversions_refactored import conversions_refactored, ConversionNotPossible


class TestConversionFunctions(unittest.TestCase):

    def test_temperature_conversions(self):
        self.assertAlmostEqual(conversions_refactored("Celsius", "Fahrenheit", 0), 32.0, places=2)
        self.assertAlmostEqual(conversions_refactored("Celsius", "Kelvin", 0), 273.15, places=2)
        self.assertAlmostEqual(conversions_refactored("Fahrenheit", "Celsius", 32), 0.0, places=2)
        self.assertAlmostEqual(conversions_refactored("Fahrenheit", "Kelvin", 32), 273.15, places=2)
        self.assertAlmostEqual(conversions_refactored("Kelvin", "Celsius", 273.15), 0.0, places=2)
        self.assertAlmostEqual(conversions_refactored("Kelvin", "Fahrenheit", 273.15), 32.0, places=2)

    def test_distance_conversions(self):
        self.assertAlmostEqual(conversions_refactored("Miles", "Yards", 1), 1760, places=2)
        self.assertAlmostEqual(conversions_refactored("Miles", "Meters", 1), 1609.34, places=2)
        self.assertAlmostEqual(conversions_refactored("Yards", "Miles", 1760), 1, places=2)
