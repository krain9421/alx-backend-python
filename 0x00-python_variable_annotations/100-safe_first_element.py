#!/usr/bin/env python3
"""Module that defines a type-annotated function appropriately"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function that takes a sequence 'lst' and
        returns the first element of the sequence if
        'lst' exists or None if 'lst' does not exist
    """
    if lst:
        return lst[0]
    else:
        return None
