import os

from tqdm import tqdm

from hsgt_db import HSGTDB
from hsgt_info import HSGT_Info
from data_formatting import DataFormatting


class SaveToSqlite:

    def __init__(self, hsgt):
        self.hsgt_info = HSGT_Info(hsgt)
        self.data_formatting = DataFormatting(hsgt)

    def save_data_to_sqlite(self, content):
        hsgt_db = HSGTDB()
        hsgt_db.connect()
        hsgt_db.insert_data(content)

    def save_file_to_sqlite(self, file_name):
        items = self.data_formatting.extract_items_in_file(file_name)
        print(items)
        self.save_data_to_sqlite(items)

    def save_all_files_to_sqlite(self):
        print(self.hsgt_info.name())
        file_list = [
            f for f in os.listdir(
                self.hsgt_info.folder()) if '.txt' in f]

        for f in tqdm(file_list):
            file_name = os.path.join(self.hsgt_info.folder(), f)
            self.save_file_to_sqlite(file_name)
