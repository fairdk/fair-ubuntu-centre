#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""rm /etc/computer_label_id""",]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 10s this script will remove label registrations on all machines"
    time.sleep(10)
    deploy(COMMANDS)


