#!/usr/bin/env python3
"""
7-to_kv
"""


def to_kv(k: str, v: float | int) -> tuple[str, float]:
    """to string and square"""
    return (k, v * v)
