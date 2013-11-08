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
    print "In 5s this script will start sending a printer configuration file to alle clients."
    time.sleep(5)
    sendfile("printers.conf", "/etc/cups/printers.conf")
    sendfile("printer-1.ppd", "/etc/cups/ppd/printer-1.ppd")
    deploy(["/etc/init.d/cups restart"])


