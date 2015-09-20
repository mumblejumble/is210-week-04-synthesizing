#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1"""


import decimal


ABSOLUTE_DIFFERENCE = decimal.Decimal('271.15')


def celsius_to_kelvin(degrees):
    """converting a Celsius temperature to Kelvin"""
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees


def fahrenheit_to_celsius(degrees):
    """converting fahrenheit to celsius."""
    degrees = (decimal.Decimal(degrees) - 32) * 5 / 9
    return degrees


def fahrenheit_to_kelvin(degrees):
    """converting a Fahrenheit temperature to Kelvin"""
    degrees = (decimal.Decimal(degrees) - 32) * 5 / 9
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees
