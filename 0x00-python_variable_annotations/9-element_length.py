#!/usr/bin/env python3
"""
9-element_length
"""


from typing import List, Tuple


def element_length(lst: float) -> List[Tuple[]]:
    return [(i, len(i)) for i in lst]
