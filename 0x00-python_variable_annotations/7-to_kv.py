#!/usr/bin/env python3
"""
7-to_kv
"""


from typing import Tuple, Union 


def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """to string and square"""
    return (k, v * v)
