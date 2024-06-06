#!/usr/bin/env python3
"""Module that defines a type-annotated function `sum_mixed_list`"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Function which takes a list 'mxd_lst'
        of integers and floats as argument and
        returns their sum as a float.
    """
    return sum(mxd_lst)
