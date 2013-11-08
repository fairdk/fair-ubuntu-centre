#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = ["""rm /home/student/Desktop/Materials\\ for\\ Students""",
                """rm /home/teacher/Desktop/Materials\\ for\\ Students""",]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 20s this script will start to ask all clients to shutdown!"
#    time.sleep(20)
    deploy(COMMANDS)


