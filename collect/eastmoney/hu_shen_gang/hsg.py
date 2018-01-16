#!/usr/bin/env python3

import logging
import os
import sys
from logging import config

import yaml

from command_hsg import CommandHSG
from subcmds import all_commands

# load logging config
CODE_PATH = os.path.dirname(os.path.abspath(__file__))
with open(CODE_PATH + '/log/logging.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)

# disable pyshark's log
logger_trollius = logging.getLogger('trollius')
logger_trollius.addHandler(logging.NullHandler())
logger_trollius.propagate = False


if '__main__' == __name__:
    print(sys.argv[1:])
    print(all_commands)

    cmd = all_commands[sys.argv[1]]()
    cmd.execute()
