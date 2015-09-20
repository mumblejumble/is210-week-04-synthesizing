#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1"""


from decimal import Decimal


ABSOLUTE_DIFFERENCE = Decimal('273.15')


def celsius_to_kelvin(degrees):
    """converting a Celsius temperature to Kelvin"""
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees


def fahrenheit_to_celsius(degrees):
    """converting fahrenheit to celsius."""
    degrees = (Decimal(degrees) - 32) * 5 / 9
    return degrees


def fahrenheit_to_kelvin(degrees):
    """converting a Fahrenheit temperature to Kelvin"""
    degrees = (Decimal(degrees) - 32) * 5 / 9
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees
