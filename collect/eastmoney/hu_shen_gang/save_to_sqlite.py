import json
import logging
import os

from tqdm import tqdm

from hsgt_db import HSGTDB


class SaveToSqlite:
    HSG_INFO = 'hsg.json'

    def __init__(self):
        self.hsg_info = self.get_json()

    def get_json(self):
        if os.path.exists(self.HSG_INFO):
            with open(self.HSG_INFO, 'r') as f:
                return json.load(f)
        else:
            logging.error('Missed file: ' + self.HSG_INFO)

    def get_original_str(self, file_name):
        if os.path.exists(self.HSG_INFO):
            with open(file_name, 'r') as f:
                return f.read()
        else:
            return ''

    def get_useful_str(self, original_str):
        useful_begin = self.hsg_info['hgt'][0]['useful_begin']
        useful_end = self.hsg_info['hgt'][0]['useful_end']
        return original_str[useful_begin:useful_end]

    def get_item(self, data):
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

    def str_to_list(self, string):
        data = json.loads(string)
        items = []
        for datum in data:
            items.append(self.get_item(datum))
        return items

    def save_content_to_sqlite(self, content):
        hsgt_db = HSGTDB()
        hsgt_db.connect()
        hsgt_db.insert_data(content)

    def save_file_to_sqlite(self, file_name):
        original_str = self.get_original_str(file_name)
        useful_str = self.get_useful_str(original_str)
        content = self.str_to_list(useful_str)
        self.save_content_to_sqlite(content)

    def process_all_files_in_folder(self, folder):
        file_list = [
            f for f in os.listdir(
                folder) if '.txt' in f]
        for f in tqdm(file_list):
            file_name = os.path.join(folder, f)
            self.save_file_to_sqlite(file_name)

    def process_all_folders(self):
        for hsg in self.hsg_info:
            print(self.hsg_info[hsg][0]['name'])
            self.process_all_files_in_folder(self.hsg_info[hsg][0]['folder'])


if '__main__' == __name__:
    sts = SaveToSqlite()
    sts.process_all_folders()
