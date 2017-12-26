import json
import sys

from hu_shen_gang_tong import HuShenGangTong
from task import Task


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
        pass
    elif len(sys.argv) > 1 and 'update' == sys.argv[1]:
        fund_manager.update()
        pass
    else:
        fund_manager.process_tasks()
