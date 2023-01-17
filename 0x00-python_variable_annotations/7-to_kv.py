#!/usr/bin/env python3
"""
7-to_kv
"""


from typing import Tuple 


def to_kv(k: str, v: float | int) -> Tuple[str, float]:
    """to string and square"""
    return (k, v * v)
