#!usr/bin/env python3
"""
6-sum_mixed_list
"""


def sum_mixed_list(input_list: list[float | int]) -> float:
    res: float = 0
    for n in input_list:
        res = res + n
    return (res)
