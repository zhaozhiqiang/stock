import json
import os

from hsgt_info import HSGT_Info
from time import strptime


class DataFormatting:

    def __init__(self, hsgt):
        self.hsgt_info = HSGT_Info(hsgt)

    def get_original_str(self, file_name):
        with open(file_name, 'r') as f:
            return f.read()

    def get_useful_str(self, original_str):
        useful_begin = self.hsgt_info.useful_begin()
        useful_end = self.hsgt_info.useful_end()
        return original_str[useful_begin:useful_end]

    def extract_one_line_value(self, data):
        item = []
        item.append(data['HDDATE'][:-9])
        item.append(data['SCODE'])
        item.append(data['SNAME'])
        item.append(data['CLOSEPRICE'])
        item.append(data['ZDF'])
        item.append(data['SHAREHOLDPRICE'])
        item.append(data['SHARESRATE'])
        item.append(data['SHAREHOLDPRICE'])
        item.append(data['SHAREHOLDPRICEONE'])
        item.append(data['SHAREHOLDPRICEFIVE'])
        item.append(data['SHAREHOLDPRICETEN'])
        return item

    def is_new_datum(self, datum):
        return strptime(datum['HDDATE'][:-9], "%Y-%m-%d") > strptime(self.hsgt_info.last_date(), "%Y-%m-%d")

    def extract_all_lines_value(self, string):
        data = json.loads(string)
        items = []
        for datum in data:
            if not self.is_new_datum(datum):
                continue
            items.append(self.extract_one_line_value(datum))
        return items

    def extract_items_in_file(self, file_name):
        original_str = self.get_original_str(file_name)
        useful_str = self.get_useful_str(original_str)
        return self.extract_all_lines_value(useful_str)
