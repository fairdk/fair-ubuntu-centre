#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

COMMANDS = ["""gnome-text-editor -display :0"""]

from deploy import deploy, sendfile

if __name__ == '__main__':
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 20s this script will try to spawn a text editor on all active desktops as a test."
    time.sleep(20)
    deploy(COMMANDS)


