import json
import logging
import os
import sys
from time import sleep

import requests
from tqdm import tqdm

from task import Task


class HuShenGang(Task):
    link_info = {}
    data_status = {}

    def __init__(self, json_file):
        self.link_info = self.get_json(json_file)
        self.data_status = dict.fromkeys(
            range(1, int(self.link_info['pages']) + 1))
        self.init_data_status()

        if not os.path.exists(self.link_info['directory']):
            os.mkdir(self.link_info['directory'])

    def init_data_status(self):
        for key, value in self.data_status.items():
            if os.path.isfile(self.get_file_path(key)):
                self.data_status[key] = True

    def get_json(self, json_file):
        if '' == json_file:
            logging.error("Need config file!")

        with open(json_file, 'r') as f:
            return json.load(f)

    def generate_link(self, index):
        return self.link_info['link_begin'] + \
            str(index) + self.link_info['link_end']

    def generate_file_name(self, index):
        mask_str = '0' * (len(str(self.link_info['pages'])) - len(str(index)))
        return mask_str + str(index) + '.txt'

    def get_file_path(self, index):
        return self.link_info['directory'] + self.generate_file_name(index)

    def requests_data(self, index):
        try:
            content = requests.get(self.generate_link(index)).text
        except requests.exceptions.Timeout as e:
            logging.error(e.message)
        self.save_to_file(
            self.get_file_path(index), content)

    def requests_all_data(self):
        print(self.link_info['name'])
        for key, value in tqdm(self.data_status.items()):
            if value is None:
                self.requests_data(int(key))

    def clear(self):
        file_list = [
            f for f in os.listdir(
                self.link_info['directory']) if '.txt' in f]
        for f in file_list:
            os.remove(os.path.join(self.link_info['directory'], f))
