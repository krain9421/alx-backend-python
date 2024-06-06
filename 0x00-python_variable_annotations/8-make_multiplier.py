#!/usr/bin/env python3
"""Module that defines a type-annotated function 'make_multiplier'"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function which takes takes a float
        'multiplier' as argument and returns
        a function that multiplies a float by 'multiplier'
    """
    def multiply(num: float) -> float:
        """Callback function 'multiply'"""
        return num * multiplier

    return multiply
