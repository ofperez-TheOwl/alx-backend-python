#!/usr/bin/env python3
"""
9-element_length
"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element length"""
    return [(i, len(i)) for i in lst]
