from command_hsg import CommandHSG


class Init(CommandHSG):
    common = True
    helpSummary = '''
Delete cache data, download latest data and save them to sqlite'''
    helpUsage = 'stock init'

    def __init__(self):
        self.clear = Clear()

    def execute(self):
        self.clear.execute()
        for task in self.tasks:
            task.requests_all_data()