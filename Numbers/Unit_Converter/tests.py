#!/usr/bin/env python3
import unittest

from Numbers.Unit_Converter.unit_converter import Metre, Inch, Foot, Yard, Mile, Kilogram, Pound, \
    Ounce, Second, Minute, Hour, Day, Kelvin, Celsius, Fahrenheit


class Test(unittest.TestCase):
    def test_convert_to_base_of_length(self):
        self.assertEqual(Metre(1).convert_to_base().value, Metre(1).value)
        self.assertEqual(Inch(1).convert_to_base().value, Metre(0.0254).value)
        self.assertEqual(Foot(1).convert_to_base().value, Metre(0.3048).value)
        self.assertEqual(Yard(1).convert_to_base().value, Metre(0.9144).value)
        self.assertEqual(Mile(1).convert_to_base().value, Metre(1609.344).value)

    def test_convert_to_base_of_mass(self):
        self.assertEqual(Kilogram(1).convert_to_base().value, Kilogram(1).value)
        self.assertEqual(Pound(1).convert_to_base().value, Kilogram(0.45359237).value)
        self.assertEqual(Ounce(1).convert_to_base().value, Kilogram(0.028349523125).value)

    def test_convert_to_base_of_time(self):
        self.assertEqual(Second(1).convert_to_base().value, Second(1).value)
        self.assertEqual(Minute(1).convert_to_base().value, Second(60).value)
        self.assertEqual(Hour(1).convert_to_base().value, Second(3600).value)
        self.assertEqual(Day(1).convert_to_base().value, Second(86400).value)

    def test_convert_to_base_of_temperature(self):
        self.assertEqual(Kelvin(0).convert_to_base().value, Kelvin(0.0).value)
        self.assertEqual(Celsius(0).convert_to_base().value, Kelvin(273.15).value)
        self.assertEqual(Fahrenheit(0).convert_to_base().value, Kelvin(255.37222222222223).value)

    def test_convert_from_base_of_length(self):
        self.assertEqual(Metre(1).convert_from_base(1).value, Metre(1).value)
        self.assertEqual(Inch(1).convert_from_base(1).value, Inch(39.37007874015748).value)
        self.assertEqual(Foot(1).convert_from_base(1).value, Foot(3.280839895013123).value)
        self.assertEqual(Yard(1).convert_from_base(1).value, Yard(1.0936132983377078).value)
        self.assertEqual(Mile(1).convert_from_base(1).value, Mile(0.0006213711922373339).value)

    def test_convert_from_base_of_mass(self):
        self.assertEqual(Kilogram(1).convert_from_base(1).value, Kilogram(1).value)
        self.assertEqual(Pound(1).convert_from_base(1).value, Pound(2.2046226218487757).value)
        self.assertEqual(Ounce(1).convert_from_base(1).value, Ounce(35.27396194958041).value)

    def test_convert_from_base_of_time(self):
        self.assertEqual(Second(1).convert_from_base(1).value, Second(1).value)
        self.assertEqual(Minute(1).convert_from_base(1).value, Minute(0.016666666666666666).value)
        self.assertEqual(Hour(1).convert_from_base(1).value, Hour(0.0002777777777777778).value)
        self.assertEqual(Day(1).convert_from_base(1).value, Day(1.1574074074074073e-05).value)

    def test_convert_from_base_of_temperature(self):
        self.assertEqual(Kelvin(0).convert_from_base(0).value, Kelvin(0).value)
        self.assertEqual(Celsius(0).convert_from_base(0).value, Celsius(-273.15).value)
        self.assertEqual(Fahrenheit(0).convert_from_base(0).value, Fahrenheit(-459.67).value)


if __name__ == "__main__":
    unittest.main()
