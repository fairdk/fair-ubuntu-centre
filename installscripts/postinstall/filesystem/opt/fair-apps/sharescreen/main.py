#!/usr/bin/python
import gtk
import datetime
import os
import subprocess, shlex
import re
import time

gtk.gdk.threads_init() #@UndefinedVariable

BASE_PATH = os.path.dirname(__file__)

VNC_PORT = 5900
REMOTE_START_VNC = "ssh -o CheckHostIP=no -o StrictHostKeyChecking=no student@%s \"vncviewer -Shared -ViewOnly -FullScreen -UseLocalCursor=0 %s:%d\" -display :0"
REMOTE_STOP_VNC = "killall vncviewer"
LOCAL_START_VNC = "x11vnc -viewonly -shared -shared -forever"# % VNC_PORT

#REMOTE_IPS = ["192.168.10.106"]
REMOTE_IPS = ["192.168.10.%d" % x for x in xrange(10,256)]

from settings import *

def get_ips():
    global ETH
    co = subprocess.Popen(['ifconfig', ETH], stdout = subprocess.PIPE)
    ifconfig = co.stdout.read()
    ip_regex = re.compile('((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-5][0-9]|[01]?[0-9][0-9]?))')
    return [match[0] for match in ip_regex.findall(ifconfig, re.MULTILINE)]

class MainWindow():
    
    def __init__(self):
        
        self.glade = gtk.Builder()
        self.glade.add_from_file(os.path.join(BASE_PATH, 'glade', 'mainwindow.glade'))
        
        self.win = self.glade.get_object("mainwindow")
        self.win.show_all()
        
        self.win.connect("delete-event", self.on_delete_event)
        self.win.connect('destroy', self.on_destroy)

        self.glade.connect_signals(self)
        
        self.x11vnc_alive = False
        self.start_vncserver()
        
        self.connect_processes = []
        
        try:
            self.external_ip = get_ips()[0]
            self.log("My IP address is: %s" % self.external_ip)
        except IndexError:
            self.get_widget("button_start").set_sensitive(False)
            self.log("Network is not running")
        
    def start_vncserver(self):
        if self.x11vnc_alive: return
        self.x11vnc_alive = True
        self.x11vnc_process = subprocess.Popen(shlex.split(LOCAL_START_VNC))
        self.log("Started the X11 server and listening for connections...")        
        
    def get_widget(self, key):
        return self.glade.get_object(key)
    
    def on_delete_event(self, *args):
        """
        Display manager closed window.
        """
        self.x11vnc_alive = False
        for p in self.connect_processes:
            p.terminate()
            time.sleep(0.1)
        self.x11vnc_process.terminate()
        self.win.destroy()
        gtk.main_quit()

    def on_destroy(self, *args):
        self.alive = False

    def on_start(self, *args):
        self.get_widget("button_stop").set_sensitive(True)
        self.get_widget("button_start").set_sensitive(False)
        if not self.x11vnc_alive:
            self.start_vncserver()

        self.log("Starting to connect. %d addresses in range." % len(REMOTE_IPS))
        for ip in REMOTE_IPS:
            if not self.x11vnc_alive: return
            if ip == self.external_ip: continue
            ssh_exec = subprocess.Popen(shlex.split(REMOTE_START_VNC % (ip, self.external_ip,
                                                                        VNC_PORT)),
                                        stdout=None)
            self.connect_processes.append(ssh_exec)
            time.sleep(0.1)

    def on_stop(self, *args):
        self.log("Stopped.")
        self.x11vnc_process.terminate()
        self.x11vnc_alive = False
        for p in self.connect_processes:
            p.kill()
        for ip in REMOTE_IPS:
            if ip == self.external_ip: continue
            ssh_exec = subprocess.Popen(shlex.split(REMOTE_STOP_VNC), stdout=None)
        self.get_widget("button_start").set_sensitive(True)        
        self.get_widget("button_stop").set_sensitive(False)

    def log(self, msg):
        now = datetime.datetime.now()
        buffer = self.get_widget('textbuffer_log')
        buffer.insert(buffer.get_end_iter(), "[%s] %s\n" % (now.strftime("%H:%M"), msg))
    
    def connect_tread(self, ip):
        os.system("ssh")
    
if __name__ == '__main__':
    
    mainwindow = MainWindow()
    gtk.main()
    
    
    
