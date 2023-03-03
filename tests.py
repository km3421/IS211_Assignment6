import unittest
import conversions


# Because of how...unique this is, I couldn't compress it like I did in assignment 4. Or maybe I could?
# Be sure to let me know

class TestConversions(unittest.TestCase):
    def test_CelsiusToKelvin(self):
        self.assertAlmostEqual(conversions.CelsiusToKelvin(0.0), 273.15, places=2, msg="0.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToKelvin(-40.0), 233.15, places=2, msg="-40.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToKelvin(100.0), 373.15, places=2, msg="100.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToKelvin(37.0), 310.15, places=2, msg="37.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToKelvin(-273.15), 0.0, places=2, msg="-273.15 C has Failed")

    def test_CelsiusToFahrenheit(self):
        self.assertAlmostEqual(conversions.CelsiusToFahrenheit(0.0), 32.0, places=2, msg="0.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToFahrenheit(-40.0), -40.0, places=2, msg="-40.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToFahrenheit(100.0), 212.0, places=2, msg="100.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToFahrenheit(37.0), 98.6, places=2, msg="37.0 C has Failed")
        self.assertAlmostEqual(conversions.CelsiusToFahrenheit(-273.15), -459.67, places=2, msg="-273.15 C has Failed")

    def test_FahrenheitToCelsius(self):
        self.assertAlmostEqual(conversions.FahrenheitToCelsius(0.0), -17.78, places=2, msg="0.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToCelsius(-40.0), -40.0, places=2, msg="-40.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToCelsius(100.0), 37.78, places=2, msg="100.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToCelsius(37.0), 2.78, places=2, msg="37.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToCelsius(-273.15), -169.53, places=2, msg="-273.15 F has Failed")

    def test_FahrenheitToKelvin(self):
        self.assertAlmostEqual(conversions.FahrenheitToKelvin(0.0), 255.37, places=2, msg="0.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToKelvin(-40.0), 233.15, places=2, msg="-40.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToKelvin(100.0), 310.93, places=2, msg="100.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToKelvin(37.0), 275.93, places=2, msg="37.0 F has Failed")
        self.assertAlmostEqual(conversions.FahrenheitToKelvin(-273.15), 103.62, places=2, msg="-273.15 F has Failed")

    def test_KelvinToCelsius(self):
        self.assertAlmostEqual(conversions.KelvinToCelsius(0.0), -273.15, places=2, msg="0.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToCelsius(-40.0), -313.15, places=2, msg="-40.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToCelsius(100.0), -173.15, places=2, msg="100.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToCelsius(37.0), -236.15, places=2, msg="37.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToCelsius(-273.15), -546.3, places=2, msg="-273.15 K has Failed")

    def test_KelvinToFahrenheit(self):
        self.assertAlmostEqual(conversions.KelvinToFahrenheit(0.0), -459.67, places=2, msg="0.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToFahrenheit(-40.0), -531.67, places=2, msg="-40.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToFahrenheit(100.0), -279.67, places=2, msg="100.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToFahrenheit(37.0), -393.07, places=2, msg="37.0 K has Failed")
        self.assertAlmostEqual(conversions.KelvinToFahrenheit(-273.15), -951.34, places=2, msg="-273.15 K has Failed")

    def test_MilesToYards(self):
        self.assertAlmostEqual(conversions.MilesToYards(1.0), 1760, places=2, msg="1.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToYards(40.0), 70400, places=2, msg="40.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToYards(100.0), 176000, places=2, msg="100.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToYards(37.0), 65120, places=2, msg="37.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToYards(273), 480480, places=2, msg="273 MI has Failed")

    def test_MilesToMeters(self):
        self.assertAlmostEqual(conversions.MilesToMeters(1.0), 1609.0, places=2, msg="1.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToMeters(40.0), 64360, places=2, msg="40.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToMeters(100.0), 160900, places=2, msg="100.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToMeters(37.0), 59533, places=2, msg="37.0 MI has Failed")
        self.assertAlmostEqual(conversions.MilesToMeters(273), 439257, places=2, msg="273 MI has Failed")

    def test_YardsToMiles(self):
        self.assertAlmostEqual(conversions.YardsToMiles(10000.0), 5.68, places=2, msg="10000.0 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMiles(40000.0), 22.73, places=2, msg="40000.0 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMiles(100000.0), 56.82, places=2, msg="100000.0 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMiles(370000.0), 210.23, places=2, msg="370000.0 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMiles(2730000), 1551.14, places=2, msg="2730000 YA has Failed")

    def test_YardsToMeters(self):
        self.assertAlmostEqual(conversions.YardsToMeters(10000.0), 9140.77, places=2, msg="10000 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMeters(40000.0), 36563.07, places=2, msg="40000 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMeters(100000.0), 91407.68, places=2, msg="100000 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMeters(370000.0), 338208.41, places=2, msg="370000 YA has Failed")
        self.assertAlmostEqual(conversions.YardsToMeters(2730000), 2495429.62, places=2, msg="2730000 YA has Failed")

    def test_MetersToMiles(self):
        self.assertAlmostEqual(conversions.MetersToMiles(10000.0), 6.22, places=2, msg="10000.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToMiles(40000.0), 24.86, places=2, msg="40000.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToMiles(100000.0), 62.15, places=2, msg="100000.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToMiles(370000.0), 229.96, places=2, msg="370000.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToMiles(2730000), 1696.71, places=2, msg="2730000.0 M has Failed")

    def test_MetersToYards(self):
        self.assertAlmostEqual(conversions.MetersToYards(1.0), 1.09, places=2, msg="1.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToYards(40.0), 43.76, places=2, msg="40.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToYards(100.0), 109.4, places=2, msg="100.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToYards(37.0), 40.48, places=2, msg="37.0 M has Failed")
        self.assertAlmostEqual(conversions.MetersToYards(273), 298.66, places=2, msg="273 M has Failed")

# each function name is in of itself self-descriptive.
# it was, to a point, monotonous making them.
