#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Degree Conversions"""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """This function converts a Celsius temperature to Kelvin.

    Args:
        degrees (int): the degree number to be converted to celsius.

    Returns:
        a degree in celsius

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(190)
        Decimal('87.77777777777777777777777778')
    """
    celsius = (decimal.Decimal(degrees) - 32) * 5 / 9
    return celsius


def celsius_to_kelvin(degrees):
    """This function converts a Celsius temperature to Kelvin.

    Args:
        degrees (int): the degree number to be converted to Kelvin.

    Returns:
        converted degree in Kelvin

    Examples:
        >>> fahrenheit_to_kelvin(100)
        Decimal('373.15')


        >>> fahrenheit_to_celsius(200)
        Decimal('472.15')
    """
    kelvin = decimal.Decimal(ABSOLUTE_DIFFERENCE) + degrees
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """Function converts a Fahrenheit temperature to Kelvin.

    Args:
        degrees(int): degrees to be converted to kelvin.

    Returns:
        degrees in kelvin.

    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.15')

        >>> fahrenheit_to_kelvin(41)
        Decimal('230.69')
    """
    kelvin = celsius_to_kelvin(fahrenheit_to_celsius(degrees))
    return kelvin
