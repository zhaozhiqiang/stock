import json
import logging
import os

import requests
from tqdm import tqdm

from hsgt_info import HSGT_Info
from task import Task


class HuShenGangTong(Task):
    json_file = 'hsg.json'

    def __init__(self, hsgt):
        self.hsgt_info = HSGT_Info(hsgt)
        self.data_status = dict.fromkeys(
            range(1, int(self.hsgt_info.pages()) + 1))
        self.init_data_status()

        if not os.path.exists(self.hsgt_info.folder()):
            os.mkdir(self.hsgt_info.folder())

    def init_data_status(self):
        for key, value in self.data_status.items():
            if os.path.isfile(self.get_file_path(key)):
                self.data_status[key] = True

    def generate_file_name(self, index):
        mask_str = '0' * (len(str(self.hsgt_info.pages())) - len(str(index)))
        return mask_str + str(index) + '.txt'

    def get_file_path(self, index):
        return os.path.join(self.hsgt_info.folder(), self.generate_file_name(index))

    def requests_data(self, index):
        try:
            page_link = self.hsgt_info.page_link(index)
            content = requests.get(page_link).text
        except requests.exceptions.Timeout as e:
            logging.error(e.message)
        self.save_to_file(
            self.get_file_path(index), content)

    def requests_all_data(self):
        print(self.hsgt_info.name())
        for key, value in tqdm(self.data_status.items()):
            if value is not True:
                self.requests_data(int(key))

    def clear(self):
        file_list = [
            f for f in os.listdir(
                self.hsgt_info.folder()) if '.txt' in f]
        for f in file_list:
            os.remove(os.path.join(self.hsgt_info.folder(), f))
