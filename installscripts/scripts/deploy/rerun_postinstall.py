#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

from deploy import deploy, sendfile

# REMEMBER THAT SCRIPTS SHOULD NOT OUTPUT SOMETHING BACK TO SSH
# - it breaks sockets on a lot of output!!

COMMANDS = ["echo running postinstall... && sh /root/rerun-postinstall.sh > /var/log/postinstall.log 2>&1"]

if __name__ == '__main__':
    ssh_exec = subprocess.Popen(shlex.split("rm -f /root/.ssh/known_hosts"),
                                            stdout=subprocess.PIPE)
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 10s this script will start to ask all clients to download and rerun the postinstallation."
    time.sleep(10)
    sendfile("rerun-postinstall.sh", "/root/rerun-postinstall.sh")
    deploy(COMMANDS)


