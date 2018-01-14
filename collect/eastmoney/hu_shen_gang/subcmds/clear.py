from command_hsg import CommandHSG


class Clear(CommandHSG):
    common = True
    helpSummary = 'Clean cache data'
    helpUsage = 'stock clean'
    
    def execute(self):
        for task in self.tasks:
            task.clear()

