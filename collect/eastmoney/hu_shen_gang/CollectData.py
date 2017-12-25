from task import Task


class CollectData:
    def __init__(self, tasks=None):
        if tasks is None:
            tasks = []
        self.tasks = tasks

    def process_tasks(self):
        for task in self.tasks:
            task.requests_all_data()

    def initialize(self):
        for task in self.tasks:
            task.clear()
            task.requests_all_data()

    def clear(self):
        for task in self.tasks:
            task.clear()
