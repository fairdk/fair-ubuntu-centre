import datetime
import os
import subprocess, shlex
import re
import sys
import time

REMOTE_SSH_EXEC = "ssh -o CheckHostIP=no -o StrictHostKeyChecking=no -o PasswordAuthentication=no root@%s \"%s\""
REMOTE_SCP = "scp -o CheckHostIP=no -o StrictHostKeyChecking=no %s root@%s:%s"

REMOTE_IPS = ["192.168.10.%d" % x for x in xrange(20,255)]

COMMANDS = ["""sed -i 's/^.*nfs.*$//g' /etc/fstab""",]

RESPONSE_ERROR = re.compile(r"(No\sroute\sto\shost|Connection\srefused|Permission\sdenied|Network\sis\sunreachable)")

# Some old example...
def deploy_sequential(cmds):
    ssh_exec = subprocess.Popen(shlex.split("rm /root/.ssh/known_hosts"),
                                            stdout=subprocess.PIPE)
    success = 0
    for ip in REMOTE_IPS:
            for cmd in cmds:
                ssh_exec = subprocess.Popen(shlex.split(REMOTE_SSH_EXEC % (ip, cmd)),
                                            stdout=subprocess.PIPE)
                response = ssh_exec.stdout.read()
                if "No route to host" in response or "Connection refused" in response or "Permission denied" or "Network is unreachable" in response:
                    pass
                else:
                    success = success + 1
    
    return ssh_exec, success
    
def deploy(cmds):
    ssh_exec = subprocess.Popen(shlex.split("rm /root/.ssh/known_hosts"),
                                            stdout=subprocess.PIPE)
    for ip in REMOTE_IPS:
        for cmd in cmds:
            ssh_exec = subprocess.Popen(shlex.split(REMOTE_SSH_EXEC % (ip, cmd)),
                                        stdout=subprocess.PIPE)

def sendfile(src, dst):
    ssh_exec = subprocess.Popen(shlex.split("rm ~/.ssh/known_hosts"),
                                            stdout=subprocess.PIPE)

    for ip in REMOTE_IPS:
        ssh_exec = subprocess.Popen(shlex.split(REMOTE_SCP % (src, ip, dst)),
                                    stdout=subprocess.PIPE)


