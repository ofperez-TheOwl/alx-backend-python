#!usr/bin/env python3
"""
5-sum_list
"""


def sum_list(input_list: list[float]) -> float:
    res: float = 0
    for n in input_list:
        res = res + n
    return (res)
