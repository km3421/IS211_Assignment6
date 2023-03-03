def CelsiusToKelvin(celsius):
    return celsius + 273.15


def CelsiusToFahrenheit(celsius):
    return celsius * 9 / 5 + 32


def FahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def FahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def KelvinToCelsius(kelvin):
    return kelvin - 273.15


def KelvinToFahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def MilesToYards(miles):
    return miles * 1760


def MilesToMeters(miles):
    return miles * 1609


def YardsToMiles(yards):
    return yards / 1760


def YardsToMeters(yards):
    return yards / 1.094


def MetersToMiles(meters):
    return meters / 1609


def MetersToYards(meters):
    return meters * 1.094
