#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1"""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def celsius_to_kelvin(degrees):
    """converting a Celsius temperature to Kelvin
    when degrees is passed a number it's added by ABSOLUTE_DIFFERENCE"""
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees


def fahrenheit_to_celsius(degrees):
    """converting fahrenheit to celsius.
    degrees passed to Decimal. When a number is given, it's passed to
    the equation in decimal form"""
    degrees = (decimal.Decimal(degrees) - 32) * 5 / 9
    return degrees


def fahrenheit_to_kelvin(degrees):
    """converting a Fahrenheit temperature to Kelvin
    when degrees is passed a number, it's added by ABSOLUTE_DIFFERENCE,
    and then the answer is passed to degrees = (decimal.Decimal(degrees)
    - 32) * 5 / 9, calculation happens and then final answer is returned"""
    degrees = (decimal.Decimal(degrees) - 32) * 5 / 9
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees
