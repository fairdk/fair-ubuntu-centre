#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""gpasswd -a student nopasswdlogin && /etc/init.d/lightdm restart""",]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 5s this script will start to ask all clients to shutdown!"
    time.sleep(5)
    deploy(COMMANDS)


