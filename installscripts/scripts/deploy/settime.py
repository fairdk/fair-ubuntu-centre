#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""date 09111931 && hwclock -w""",]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 10s this script will start to ask all clients to shutdown!"
    time.sleep(10)
    deploy(COMMANDS)


