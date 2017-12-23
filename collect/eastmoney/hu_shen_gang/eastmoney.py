import sys

from CollectData import CollectData
from hu_shen_gang import HuShenGang
from task import Task

if '__main__' == __name__:
    tasks = [HuShenGang('./hu_gu_tong.json'),
             HuShenGang('./shen_gu_tong.json')]
    collect_data = CollectData()
    collect_data.__init__(tasks)
    if len(sys.argv) > 1 and 'init' == sys.argv[1]:
        collect_data.initialize()
    else:
        collect_data.process_tasks()
