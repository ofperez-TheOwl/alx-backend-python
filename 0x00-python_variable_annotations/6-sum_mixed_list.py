#!/usr/bin/env python3
"""
6-sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(input_list: List[Union[int, float]]) -> float:
    """sum of mixed list"""
    res: float = 0
    for n in input_list:
        res = res + n
    return (res)
