import json
import logging
import os

class HSGT_Info:

    HSGT_JSON = 'hsgt.json'
    _hsgt =''
    _info = {}
    _hsgt_info = {}

    def __init__(self, key):
        self._hsgt = key
        self._hsgt_info = self.get_hsgt_info()
        self._info = self._hsgt_info[key][0]

    def get_hsgt_info(self):
        if not os.path.exists(self.HSGT_JSON):
            logging.error('Missed file: ' + self.HSGT_JSON)

        with open(self.HSGT_JSON, 'r') as f:
            return json.load(f)

    def name(self):
        return self._info['name']

    def last_date(self):
        return self._info['last_date']

    def page_link(self, page):
        begin_length = int(self._info['begin_length'])
        end_length = int(self._info['end_length'])
        return self._info['link'][:begin_length] + \
            str(page) + self._info['link'][-end_length:]

    def pages(self):
        return self._info['pages']

    def folder(self):
        return self._info['folder']

    def useful_begin(self):
        return self._info['useful_begin']

    def useful_end(self):
        return self._info['useful_end']

    def update_hsgt_info(self, key, value):
        if not os.path.exists(self.HSGT_JSON):
            logging.error('Missed file: ' + self.HSGT_JSON)

        self._hsgt_info[self._hsgt][0][key] = value        
        with open(self.HSGT_JSON, 'w') as f:
            json.dump(self._hsgt_info, f)