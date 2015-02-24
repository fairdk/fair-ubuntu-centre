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
    print "In 2s this script will send new register_login and register_logout files"
    time.sleep(2)
    sendfile("register_login.sh", "/etc/lightdm/register_login.sh")
    sendfile("register_logout.sh", "/etc/lightdm/register_logout.sh")


