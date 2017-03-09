#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

if __name__ == '__main__':
    COMMANDS = [
        """dpkg --configure -a && apt-get -y remove usbmount""",
    ]
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 5s this script will start to ask all clients to download and rerun the postinstallation."
    time.sleep(5)
    deploy(COMMANDS)


