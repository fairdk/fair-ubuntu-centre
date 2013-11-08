#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""/usr/share/debconf/fix_db.pl > /dev/null && dpkg --configure -a""",]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 10s this script will ensure that all packages are confured after installing!"
    time.sleep(10)
    deploy(COMMANDS)


