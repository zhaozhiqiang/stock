from command_hsg import CommandHSG


class Request(CommandHSG):
    common = True
    helpSummary = '''
download latest data'''
    helpUsage = 'stock download'

    def execute(self):
        for task in self.tasks:
            task.requests_all_data()