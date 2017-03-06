import subprocess, shlex, time

REMOTE_SSH_EXEC = "ssh -o CheckHostIP=no -o StrictHostKeyChecking=no -o PasswordAuthentication=no root@%s \"%s\""
REMOTE_SCP = "scp -o CheckHostIP=no -o StrictHostKeyChecking=no %s root@%s:%s"

REMOTE_IPS = ["192.168.10.%d" % x for x in xrange(20,255)]
#REMOTE_IPS = ["192.168.10.%d" % x for x in [73]]

#COMMANDS = ["""sed -i 's/^.*nfs.*$//g' /etc/fstab""",]

def deploy(cmds, ips=None):
    #subprocess.Popen(shlex.split("rm -f ~/.ssh/known_hosts"),
    #    stdout=subprocess.PIPE)
    processes = []
    for ip in (ips or REMOTE_IPS):
        for cmd in cmds:
            subprocess.Popen(shlex.split('ssh-keygen -f "/root/.ssh/known_hosts" -R {ip:s}'.format(ip=ip)))
            processes.append(
                subprocess.Popen(shlex.split(REMOTE_SSH_EXEC % (ip, cmd)),
                    stdout=subprocess.PIPE)
            )
            time.sleep(.1)
    return processes


def sendfile(src, dst, ips=None):
    #subprocess.Popen(shlex.split("rm -f ~/.ssh/known_hosts"),
    #    stdout=subprocess.PIPE)
    processes = []
    for ip in (ips or REMOTE_IPS):
        processes.append(
            subprocess.Popen(shlex.split(REMOTE_SCP % (src, ip, dst)),
                stdout=subprocess.PIPE)
        )
    return processes
