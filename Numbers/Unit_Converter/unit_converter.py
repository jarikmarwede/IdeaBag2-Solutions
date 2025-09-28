#!/usr/bin/env python3
"""A simple pythonic unit conversion API.

Title:
Unit Converter

Description:
Develop a program that converts various units between one another.
The user enters the type of unit being entered,
the type of unit they want to convert to
and then the value.
The program will then make the conversion.
"""


class Unit:
    def __init__(self, value):
        if isinstance(value, self.__class__.__bases__[0]):  # if unit is the same
            self.value = self.convert_from_base(value.convert_to_base().value).value
        elif isinstance(value, Unit):  # if unit is not the same
            raise TypeError(f"Unit {value.__class__.__name__} can not be converted to"
                            f" {self.__class__.__name__}")
        else:  # if value is not a unit
            self.value = value

    def convert_to_base(self):
        pass

    def convert_from_base(self, value):
        pass

    def __repr__(self) -> str:
        return f"{str(self.value)} {unit_abbreviations[type(self)]}"


class Length(Unit):
    _unit_in_base: float = 1

    def convert_to_base(self):
        """Convert the current value to the base unit."""
        return Metre(self.value * self._unit_in_base)

    def convert_from_base(self, value: int):
        """Convert the input value to this unit."""
        return self.__class__(value / self._unit_in_base)

    def __add__(self, other):
        return Metre(self.convert_to_base().value + other.convert_to_base().value)

    def __sub__(self, other):
        return Metre(self.convert_to_base().value - other.convert_to_base().value)


class Mass(Unit):
    _unit_in_base: float = 1

    def convert_to_base(self):
        """Convert the current value to the base unit."""
        return Kilogram(self.value * self._unit_in_base)

    def convert_from_base(self, value: int):
        """Convert the input value to this unit."""
        return self.__class__(value / self._unit_in_base)

    def __add__(self, other):
        return Kilogram(self.convert_to_base().value + other.convert_to_base().value)

    def __sub__(self, other):
        return Kilogram(self.convert_to_base().value - other.convert_to_base().value)


class Time(Unit):
    _unit_in_base = 1

    def convert_to_base(self):
        """Convert the current value to the base unit."""
        return Second(self.value * self._unit_in_base)

    def convert_from_base(self, value: int):
        """Convert the input value to this unit."""
        return self.__class__(value / self._unit_in_base)

    def __add__(self, other):
        return Second(self.convert_to_base().value + other.convert_to_base().value)

    def __sub__(self, other):
        return Second(self.convert_to_base().value - other.convert_to_base().value)


class Temperature(Unit):
    pass


class Metre(Length):
    _unit_in_base = 1


class Inch(Length):
    _unit_in_base = 0.0254


class Foot(Length):
    _unit_in_base = 0.3048


class Yard(Length):
    _unit_in_base = 0.9144


class Mile(Length):
    _unit_in_base = 1609.344


class Kilogram(Mass):
    _unit_in_base = 1


class Pound(Mass):
    _unit_in_base = 0.45359237


class Ounce(Mass):
    _unit_in_base = 0.028349523125


class Second(Time):
    _unit_in_base = 1


class Minute(Time):
    _unit_in_base = 60


class Hour(Time):
    _unit_in_base = 3600


class Day(Time):
    _unit_in_base = 86400


class Kelvin(Temperature):
    def convert_to_base(self):
        """Convert the current value to the base unit."""
        return Kelvin(self.value)

    def convert_from_base(self, value):
        """Convert the input value to this unit."""
        return Kelvin(value)


class Celsius(Temperature):
    """Convert the current value to the base unit."""
    def convert_to_base(self):
        return Kelvin(self.value + 273.15)

    def convert_from_base(self, value):
        """Convert the input value to this unit."""
        return Celsius(value - 273.15)


class Fahrenheit(Temperature):
    """Convert the current value to the base unit."""
    def convert_to_base(self):
        return Kelvin((self.value + 459.67) * (5/9))

    def convert_from_base(self, value):
        """Convert the input value to this unit."""
        return Fahrenheit(value / (5/9) - 459.67)


unit_abbreviations = {
    Metre: "m",
    Inch: "in",
    Foot: "ft",
    Yard: "yd",
    Mile: "mi",
    Kilogram: "kg",
    Pound: "lb",
    Ounce: "oz",
    Second: "s",
    Minute: "min",
    Hour: "h",
    Day: "d",
    Kelvin: "K",
    Celsius: "°C",
    Fahrenheit: "°F"
}


def _start_interactively():
    unit_of_abbreviation = {
        "m": Metre,
        "in": Inch,
        "ft": Foot,
        "yd": Yard,
        "mi": Mile,
        "kg": Kilogram,
        "lb": Pound,
        "oz": Ounce,
        "s": Second,
        "min": Minute,
        "h": Hour,
        "d": Day,
        "K": Kelvin,
        "°C": Celsius,
        "°F": Fahrenheit
    }
    while True:
        number_to_convert = input("Please type in the number you want to convert: ")
        convert_from = input("Please type in the abbreviation for the unit of the number: ")
        convert_to = input("Please type in the abbreviation for the unit "
                           "you want the number to be converted to: ")
        try:
            if convert_from not in unit_of_abbreviation or convert_to not in unit_of_abbreviation:
                print("The conversion failed because the units are wrong."
                      "Please try again!")
            else:
                print(f"{number_to_convert} {convert_from} is",
                      unit_of_abbreviation[convert_to](
                          unit_of_abbreviation[convert_from](float(number_to_convert))
                      ))
        except TypeError:
            print("The conversion failed because the units are not of the same kind. "
                  "Please try again!")
        except ValueError:
            print("The conversion failed because the number you entered is invalid. "
                  "Please try again!")
        finally:
            print("")


if __name__ == "__main__":
    _start_interactively()
