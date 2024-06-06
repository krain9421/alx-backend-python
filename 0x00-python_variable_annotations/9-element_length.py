#!/usr/bin/env python3
"""Module that defines a type-annotated function appropriately"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that takes a list-like argument
        'lst' and returns a list of tuples that
        of the format (element, length of element) for
        each element in 'lst'
    """
    return [(i, len(i)) for i in lst]
