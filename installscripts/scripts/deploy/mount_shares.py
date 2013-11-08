#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""/etc/init.d/mount_shares start""",]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 20s this script will start to ask all clients to download and rerun the postinstallation."
    time.sleep(20)
    deploy(COMMANDS)


