#!/usr/bin/env python3
"""
The method called get_page takes two pages of arguments with
the default value of 1 and page_size with the default value of 10.
"""


import csv
import math
import requests
from typing import List


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

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a specific page from the dataset. The first page is 1.
        """
        assert isinstance(page and page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Returns a dictionary containing the following key-value pairs
        => "page_size, page, data, next_page, prev_page, prev_page"
        """
        start_index, end_index = index_range(page, page_size)
        return {
            "page_size": 0 if len(self.dataset()) <= end_index else page_size,
            "page": page,
            "data": self.dataset()[start_index:end_index],
            "next_page": None if end_index > len(self.dataset()) else page + 1,
            "prev_page": None if page <= 1 else page - 1,
            "total_pages": len(self.dataset())
        }
