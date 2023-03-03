class ConversionNotPossible(Exception):
    pass


def conversions_refactored(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value

    if fromUnit == "Celsius" and toUnit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif fromUnit == "Celsius" and toUnit == "Kelvin":
        return value + 273.15
    elif fromUnit == "Fahrenheit" and toUnit == "Celsius":
        return (value - 32) * 5 / 9
    elif fromUnit == "Fahrenheit" and toUnit == "Kelvin":
        return (value + 459.67) * 5 / 9
    elif fromUnit == "Kelvin" and toUnit == "Celsius":
        return value - 273.15
    elif fromUnit == "Kelvin" and toUnit == "Fahrenheit":
        return (value * 9 / 5) - 459.67
    elif fromUnit == "Miles" and toUnit == "Yards":
        return value * 1760
    elif fromUnit == "Miles" and toUnit == "Meters":
        return value * 1609.34
    elif fromUnit == "Yards" and toUnit == "Miles":
        return value / 1760
    elif fromUnit == "Yards" and toUnit == "Meters":
        return value / 1.094
    elif fromUnit == "Meters" and toUnit == "Miles":
        return value / 1609.34
    elif fromUnit == "Meters" and toUnit == "Yards":
        return value * 1.094
    else:
        raise ConversionNotPossible("Conversion not possible between {} and {}".format(fromUnit, toUnit))

# Turns out there was a way to do it all at once
