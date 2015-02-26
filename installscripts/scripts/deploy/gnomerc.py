#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time
from deploy import deploy, sendfile

if __name__ == '__main__':
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 2s this script will send new .gnomerc files"
    time.sleep(2)
#    sendfile(".gnomerc", "/home/teacher/.gnomerc")
#    sendfile(".gnomerc", "/home/student/.gnomerc")
    sendfile(".gnomerc", "/etc/skel/.gnomerc")


