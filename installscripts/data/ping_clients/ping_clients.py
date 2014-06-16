#!/usr/bin/python
import subprocess, shlex
import time
from datetime import datetime, timedelta
import threading
import thread
import re
import os, sys

DEBUG = False

last_reply_lock = threading.Lock()
last_reply = datetime.now()

PING_COMMAND = "ping -c 1 -W %d %s"
PING_TIMEOUT_SECONDS = 2
IP_RANGE = ['192.168.10.%d' % x for x in range(20, 255)]

INTERVAL_SECONDS = 3 * 60 # Seconds to sleep between each ping effort

HALT_ON = timedelta(seconds=10 * 60) # If no replies received for this time, shutdown

NO_REPLY = re.compile(r"100\%\spacket\sloss")

def ping_client(ip):
    global last_reply
    co = subprocess.Popen(shlex.split(PING_COMMAND % (PING_TIMEOUT_SECONDS, ip)), stdout = subprocess.PIPE)
    output = co.stdout.read()
    if NO_REPLY.search(output):
        pass
    else:
        last_reply_lock.acquire()
        last_reply = datetime.now()
        last_reply_lock.release()
        
def ping_clients():
    time.sleep(INTERVAL_SECONDS)
    threads = []
    for ip in IP_RANGE:
        now = datetime.now()
        t = threading.Thread(target=ping_client, args=(ip,))
        t.setDaemon(True)
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
    last_reply_lock.acquire()
    if (datetime.now() - last_reply) > HALT_ON:
        if DEBUG:
            print "SHUTTING DOWN!"
        else:
            co = subprocess.Popen(shlex.split("poweroff"))
            return
    else:
        print "Got response"
    last_reply_lock.release()

if __name__ == '__main__':
    fpid = os.fork()
    if fpid!=0:
        # Running as daemon now. PID is fpid
        pid_file = file("/var/tmp/ping_clients.pid", "w")
        pid_file.write(str(fpid))
        pid_file.close()
        sys.exit(0)
    while True: ping_clients()
