#!/usr/bin/env python3
"""
0-simple_helper_function
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Function docs
    """

    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
