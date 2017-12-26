import json
import sys

from hu_shen_gang_tong import HuShenGangTong
from save_to_sqlite import SaveToSqlite
from task import Task
from hsgt_db import HSGTDB
from hsgt_info import HSGT_Info


class Command:
    def __init__(self):
        self.load_hsgt()

    def load_hsgt(self):
        self.tasks = []
        self.tasks.append(HuShenGangTong('hgt'))
        self.tasks.append(HuShenGangTong('sgt'))

    def get_tasks(self):
        return self.tasks

    def process_tasks(self):
        for task in self.tasks:
            task.requests_all_data()

    def initialize(self):
        for task in self.tasks:
            task.clear()
            task.requests_all_data()

    def update(self):
        pass

    def clear(self):
        for task in self.tasks:
            task.clear()


if '__main__' == __name__:
    fund_manager = Command()
    if len(sys.argv) > 1 and 'init' == sys.argv[1]:
        fund_manager.initialize()
    elif len(sys.argv) > 1 and 'clear' == sys.argv[1]:
        fund_manager.clear()
    elif len(sys.argv) > 1 and 'update' == sys.argv[1]:
        hsgt_db = HSGTDB()
        hsgt_db.connect()
        date = hsgt_db.get_last_date()
        hgt_info = HSGT_Info('hgt')
        hgt_info.update_hsgt_info('last_date', date)
        sgt_info = HSGT_Info('sgt')
        sgt_info.update_hsgt_info('last_date', date)
    elif len(sys.argv) > 1 and 'sql' == sys.argv[1]:
        hgt = SaveToSqlite('hgt')
        sgt = SaveToSqlite('sgt')
        hgt.save_all_files_to_sqlite()
        sgt.save_all_files_to_sqlite()
    else:
        fund_manager.process_tasks()
