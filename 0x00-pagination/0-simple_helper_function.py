#!/usr/bin/env python3
"""
A function called Index_range takes two integer arguments page and page_size
"""


def index_range(page, page_size):
    """
    Returns a tuple of integers representing the range of indices
    for a given page size.
    Args:
    page (int): The current page number.
    page_size (int): The number of items to display on each page.
    """
    if page == 1:
        start_index = 0
    else:
        start_index = (page - 1) * page_size

    end_index = start_index + page_size

    return (start_index, end_index)
