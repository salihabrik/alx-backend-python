#!/usr/bin/env python3
"""
This module contains the function make_multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    
    
    """
    Takes a float multiplier as argument and returns a function that multiplies a float by multiplier.
    """
    def multiplier_func(n: float) -> float:
        return n * multiplier
    return multiplier_func

