#!/usr/bin/python
import datetime
import os
import subprocess, shlex
import re
import sys
import time

REMOTE_SSH_EXEC = "ssh -o CheckHostIP=no -o StrictHostKeyChecking=no root@%s \"%s\""
REMOTE_SCP = "scp -o CheckHostIP=no -o StrictHostKeyChecking=no %s root@%s:%s"

REMOTE_IPS = ["192.168.10.%d" % x for x in xrange(20,255)]

COMMANDS = ["""rm /home/student/Desktop/* /home/teacher/Desktop/*"""]

def deploy(cmds):
    for ip in REMOTE_IPS:
            for cmd in cmds:
                ssh_exec = subprocess.Popen(shlex.split(REMOTE_SSH_EXEC % (ip, cmd)),
                                            stdout=subprocess.PIPE)
            
def sendfile(src, dst):
    for ip in REMOTE_IPS:
            for cmd in cmds:
                ssh_exec = subprocess.Popen(shlex.split(REMOTE_SSH_EXEC % (ip, cmd)),
                                            stdout=subprocess.PIPE)

if __name__ == '__main__':
    print "MAKE SURE ALL CLIENT COMPUTERS ARE TURNED ON!"
    print "In 20s this script will start to ask all clients to reboot."
    time.sleep(20)
    deploy(COMMANDS)


