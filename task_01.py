#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 1"""


import decimal


ABSOLUTE_DIFFERENCE = decimal(271.15)


def celsius_to_kelvin(degrees):
    """converting a Celsius temperature to Kelvin"""
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees.quantize(decimal.Decimal('0.00'))


def fahrenheit_to_celsius(degrees):
    """A function that convers fahrenheit to celsius."""
    degrees = (degrees - 32) * decimal.Decimal(5) / 9
    return degrees.quantize(decimal.Decimal('0.000'))


def fahrenheit_to_kelvin(degrees):
    """converting a Fahrenheit temperature to Kelvin
    """
    degrees = (degrees - 32) * decimal.Decimal(5)/ 9
    degrees = ABSOLUTE_DIFFERENCE + degrees
    return degrees.quantize(decimal.Decimal('0.00'))
