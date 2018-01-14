from save_to_sqlite import SaveToSqlite
from command_hsg import CommandHSG


class Save(CommandHSG):
    common = True
    helpSummary = 'Save data to sqlite'
    helpUsage = 'stock save'

    def __init__(self):
        self.hgt = SaveToSqlite('hgt')
        self.sgt = SaveToSqlite('sgt')

    def execute(self):
        self.hgt.save_all_files_to_sqlite()
        self.sgt.save_all_files_to_sqlite()
