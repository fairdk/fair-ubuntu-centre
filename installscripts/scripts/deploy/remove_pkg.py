#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""dpkg --configure -a && apt-get remove -y {pkg:s}""".format(pkg=sys.argv[1]),]
    print "Going to run:\n\n"
    print "\n".join(COMMANDS)
    print "\n\n"
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 10s this script will start to ask all clients to download and rerun the postinstallation."
    time.sleep(10)
    deploy(COMMANDS)


