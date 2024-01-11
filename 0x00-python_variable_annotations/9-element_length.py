#!/usr/bin/env python3
"""
Module with a type-annotated function element_length.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function that takes an iterable object 'lst' and returns a list of tuples.
    Each tuple contains an element from 'lst' and its length.
    """
    return [(i, len(i)) for i in lst]
