#!/usr/bin/env python3

from subcmds import all_commands
from command_hsg import CommandHSG
import sys


if '__main__' == __name__:
    print(sys.argv[1:])
    print(all_commands)

    cmd = all_commands[sys.argv[1]]()
    cmd.execute()