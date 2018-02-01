from command_hsg import CommandHSG
from .request import Request
from .save import Save
from .clear import Clear
from .caplink import Caplink
from .update_data_info import UpdateDataInfo


class Update(CommandHSG):
    common = True
    helpSummary = '''
Delete cache data, download latest data and save them to sqlite'''
    helpUsage = 'stock update'

    def __init__(self):
        self.clear = Clear()
        self.request = Request()
        self.cap_link = Caplink()
        self.save = Save()
        self.update_json = UpdateDataInfo()

    def execute(self):
        self.clear.execute()
        self.cap_link.execute()
        self.request.execute()
        self.save.execute()
        self.update_json.execute()
        self.clear.execute()