#!/usr/bin/env python3
"""
Module with a type-annotated function sum_mixed_list.
"""


from typing import List, Union
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that takes a list of integers and floats and returns sums
    """
    return sum(mxd_lst)
