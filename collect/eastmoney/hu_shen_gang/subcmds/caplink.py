import logging
import os
from time import sleep

import pyshark

from command_hsg import CommandHSG
from hsgt_db import HSGTDB
from hsgt_info import HSGT_Info

INTERFACE = 'en9'
CAPTURE_TIME = 5
LAYER_HTTP = 3
GET_KEY_WORK = 'em_mutisvcexpandinterface'

HGT_JS_PATH = '~/Lab/Pacific/eastmoney/hgt_30_link.js'
SGT_JS_PATH = '~/Lab/Pacific/eastmoney/sgt_30_link.js'

logger = logging.getLogger(__name__)

class Caplink(CommandHSG):
    common = True
    helpSummary = 'Capture GET link from tshark'
    helpUsage = 'stock caplink'

    def __init__(self):
        self.task = ''

    def get_hsg_link(self, pkt):
        if 'HTTP' == pkt.highest_layer \
            and hasattr(pkt[LAYER_HTTP], 'request_full_uri') \
            and GET_KEY_WORK in pkt[LAYER_HTTP].request_full_uri:
            logger.debug(pkt[LAYER_HTTP].request_full_uri)
            self.update_link(pkt[LAYER_HTTP].request_full_uri)

    def update_link(self, link):
        hgt_info = HSGT_Info(self.task)
        hgt_info.update_hsgt_info('link', link)

    def run(self, hsgt):
        self.task = hsgt
        pid = os.fork()

        # start chromium
        if 0 == pid:
            if 'hgt' in hsgt:
                print(0)
                os.system('node ' + HGT_JS_PATH)
            else:
                print(1)
                os.system('node ' + SGT_JS_PATH)
        # start tshark
        else:
            self.cap_link()

    def execute(self):
        self.run('hgt')
        sleep(10)
        self.run('sgt')
        sleep(10)

    def cap_link(self):
        cap = pyshark.LiveCapture(interface = INTERFACE)
        cap.sniff(timeout = CAPTURE_TIME)
        l = cap.__len__()
        for i in range(0, l):
            self.get_hsg_link(cap[i])
        cap.close()