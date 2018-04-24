#!/usr/bin/python
import gtk
import datetime
import os
import subprocess, shlex
import re

import deploy

gtk.gdk.threads_init() #@UndefinedVariable

BASE_PATH = os.path.dirname(__file__)

import settings

# For looking up my IP
INTERFACES_TO_SCAN = ("eth0", "eth1", "wlan0", "em1")


def get_ips():
    for interface in INTERFACES_TO_SCAN:
        co = subprocess.Popen(['ifconfig', interface], stdout = subprocess.PIPE)
        ifconfig = co.stdout.read()
        ip_regex = re.compile('((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-4]|2[0-5][0-9]|[01]?[0-9][0-9]?))')
        ips = [match[0] for match in ip_regex.findall(ifconfig, re.MULTILINE)]
        if ips and any(map(lambda x: x.startswith(settings.IP_STARTING_WITH), ips)):
            yield ips[0]


class MainWindow():
    
    def __init__(self):
        
        self.glade = gtk.Builder()
        self.glade.add_from_file(os.path.join(BASE_PATH, 'glade', 'mainwindow.glade'))
        
        self.win = self.glade.get_object("mainwindow")
        self.win.show_all()
        
        self.win.connect("delete-event", self.on_delete_event)
        self.win.connect('destroy', self.on_destroy)

        self.glade.connect_signals(self)
        
        self.processes = []
        
        try:
            self.external_ip = list(get_ips())[0]
            self.log("My IP address is: %s" % self.external_ip)
        except IndexError:
            self.get_widget("button_shutdown").set_sensitive(False)
            self.external_ip = None
            self.log("Network is not running")
        
    def get_widget(self, key):
        return self.glade.get_object(key)
    
    def on_delete_event(self, *args):
        """
        Display manager closed window.
        """
        self.alive = False
        for p in self.processes:
            p.terminate()
        self.win.destroy()
        gtk.main_quit()

    def on_destroy(self, *args):
        pass

    def on_shutdown(self, *args):
        
        self.get_widget("button_quit").set_sensitive(False)
        
        self.alive = True
        self.log("Starting to connect. %d addresses in range. Will try to ask all these to shut down." % len(deploy.REMOTE_IPS))
        
        try:
            deploy.REMOTE_IPS.remove(self.external_ip)
        except:
            pass
        deploy.deploy(["poweroff"])
        self.log("Contacted clients and asked them to shutdown. Please confirm manually by observing the computers.")

        self.get_widget("button_quit").set_sensitive(True)

    def log(self, msg):
        now = datetime.datetime.now()
        buffer = self.get_widget('textbuffer_log')
        buffer.insert(buffer.get_end_iter(), "[%s] %s\n" % (now.strftime("%H:%M"), msg))
    
if __name__ == '__main__':
    
    mainwindow = MainWindow()
    gtk.main()
    
    
    
