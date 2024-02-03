#!/usr/bin/env python3
"""
The method called get_page takes two pages of arguments with
the default value of 1 and page_size with the default value of 10.
"""


import csv
import math
import requests
from typing import List


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
        csv_url = "https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240203%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240203T194824Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1e620cb42f7b049b2a5ec0173844ece04cf38144b2326e654b8b7bb60f68757c"

        response = requests.get(csv_url).text
        with open('Popular_Baby_Names.csv', 'a') as file:
            file.write(response)

        assert isinstance(page and page_size, int)
        assert page > 0 and page_size > 0

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)
        return dataset[start_index:end_index]

    def index_range(self, page, page_size):
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
