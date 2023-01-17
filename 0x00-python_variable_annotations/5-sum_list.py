#!/usr/bin/env python3
"""
5-sum_list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum of list"""
    res: float = 0
    for n in input_list:
        res = res + n
    return (res)
