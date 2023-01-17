#!/usr/bin/env python3
"""
9-element_length
"""


from typing import List, Tuple, Sequence


def element_length(lst: List[Sequence]) -> List[Tuple]:
    """element length"""
    return [(i, len(i)) for i in lst]
