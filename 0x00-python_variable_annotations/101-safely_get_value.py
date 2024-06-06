#!/usr/bin/env python3
"""Module that defines a function that has type annotations"""

from typing import Sequence, Any, Union, Mapping
def safely_get_value(dct: Mapping, key: Any, default: Union[~T, None] = None) -> Union[Any, ~T]:
    if key in dct:
        return dct[key]
    else:
        return default
