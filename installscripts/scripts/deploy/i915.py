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
    print "In 20s this script will send a fix for broken intel graphics support"
    time.sleep(20)
    sendfile("i915.conf", "/etc/modprobe.d/i915.conf")


