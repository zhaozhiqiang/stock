from command_hsg import CommandHSG
from hsgt_db import HSGTDB
from hsgt_info import HSGT_Info


class UpdateDataInfo(CommandHSG):
    common = True
    helpSummary = '''
Update the status of data in sqlite'''
    helpUsage = 'stock update-data-info'

    def execute(self):
        hsgt_db = HSGTDB()
        hsgt_db.connect()
        date = hsgt_db.get_last_date()
        hgt_info = HSGT_Info('hgt')
        hgt_info.update_hsgt_info('last_date', date)
        sgt_info = HSGT_Info('sgt')
        sgt_info.update_hsgt_info('last_date', date)