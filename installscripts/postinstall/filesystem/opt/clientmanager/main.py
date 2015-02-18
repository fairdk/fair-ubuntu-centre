#!/usr/bin/python
import gtk
from datetime import datetime, timedelta
import os
import subprocess
import re
import time

import deploy

import settings

gtk.gdk.threads_init() #@UndefinedVariable

BASE_PATH = os.path.dirname(__file__)
LIGHTDM_CONF = open(os.path.join(BASE_PATH, "lightdm.conf")).read()
WARNING_PY = os.path.join(BASE_PATH, "warning.py")

# Kill independent lightdm instances
# Make sure that lightdm system service is stopped'
# Wait for one second ("Failed to use bus name org.freedesktop.DisplayManager, do you have appropriate permissions?")
# Then start lightdm with nohup
REMOTE_START_SESSION = ["killall lightdm ; stop lightdm ; kill `pidof X` ; sleep 1s ; lightdm --config=/etc/lightdm/autologin.conf --pid-file=/tmp/lightdm.pid"]
REMOTE_STOP_SESSION = ["killall lightdm ; kill `pidof X` ; sleep 1s ; start lightdm"]
REMOTE_START_KILL = (
    "echo 'sleep {duration:d}m && (" + REMOTE_STOP_SESSION[0] + ")'"
    " > /tmp/lightdm_kill && nohup sh /tmp/lightdm_kill"
)
REMOTE_STOP_KILL = "pkill -f '/tmp/lightdm_kill'"
REMOTE_START_WARN = (
    "echo '#!/bin/sh' > /tmp/lightdm_warn && echo '(sleep {duration:d}m && python /tmp/warning.py) &'"
    " >> /tmp/lightdm_warn && chmod +x /tmp/lightdm_warn && mkdir -p /home/{username:s}/.config/autostart && chown -R {username:s}.{username:s} /home/{username:s}/.config && echo '' > /home/{username:s}/.config/autostart/warning.desktop && echo '[Desktop Entry]' >> /home/{username:s}/.config/autostart/warning.desktop && echo 'Type=Application' >> /home/{username:s}/.config/autostart/warning.desktop && echo 'Exec=/tmp/lightdm_warn' >> /home/{username:s}/.config/autostart/warning.desktop && echo 'Name=Warning' >> /home/{username:s}/.config/autostart/warning.desktop && echo 'Hidden=false' >> /home/{username:s}/.config/autostart/warning.desktop && echo 'NoDisplay=false' >> /home/{username:s}/.config/autostart/warning.desktop && echo 'X-GNOME-Autostart-enabled=true' >> /home/{username:s}/.config/autostart/warning.desktop"
)
REMOTE_STOP_WARN = "pkill -f '/tmp/lightdm_warn'"

# For looking up my IP
INTERFACES_TO_SCAN = ("eth0", "eth1", "wlan0")


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
        
        self.glade.get_object("spinbuttonComputer").set_range(1,len(settings.computers))
        self.glade.get_object("buttonStart").set_sensitive(False)
        
        cell = gtk.CellRendererText()
        combobox = self.glade.get_object("comboboxSession")
        combobox.pack_start(cell, True)
        combobox.add_attribute(cell, 'text', 0)
        self.sessions = {}
        for name,session in settings.sessions.items():
            for duration in session[1]:
                key = "{:s} ({:d} minutes)".format(name,duration)
                self.sessions[key] = {
                    'name': key,
                    'username': session[0],
                    'duration': duration,
                    'session_entry': session,
                    'credits_cost': duration * session[2],
                }
                self.glade.get_object("liststoreSession").append((key,))
        combobox.set_active(0)
        self.log("Starting client manager, {date:s}".format(date=str(datetime.now().date())))
        
        try:
            self.external_ip = get_ips()[0]
            self.log("My IP address is: %s" % self.external_ip)
        except IndexError:
            self.log("Network is not running")
        
        self.started_clients={}
        
    def start_client(self, computer_no, session_k, person):
        
        computer = settings.computers[computer_no]
        ip = computer[1]
        name = computer[0]
        session = self.sessions[session_k]
        
        end = datetime.now()+timedelta(minutes=session['duration'])
        
        def do_start(credits_left, extension=False):
            self.log('{person:s} now has {credits:d} credits left today'.format(person=person, credits=credits_left))
            self.kill_timeout(ip)
            self.start_timeout(ip, session['duration'], session['username'])
            if not extension:
                self.start_lightdm(ip, session)
            self.started_clients[computer_no] = {
                'end': end,
                'username': session['username'],
            }
            self.log('{person:s} now has {credits:d} credits left today'.format(person=person, credits=credits_left))
        
        
        if computer_no in self.started_clients:
            if self.started_clients[computer_no].get('username', None) == session['username']:
                if self.started_clients[computer_no].get('end', None) > datetime.now():
                    extension_lenght = int((
                        datetime.now() - self.started_clients[computer_no]['end']
                    ).total_seconds() // 60) + session['duration']
                    self.log(
                        "'{name:s}' already started - extending {session:s}"
                        " duration until {end:s} for student {person:s}".format(
                            end=str(end),
                            name=name,
                            session=session['name'],
                            person=person,
                        )
                    )
                    credits_left = 0
                    try:
                        credits_left = settings.save_usage(person, extension_lenght)
                        do_start(credits_left, extension=True)
                    except settings.NoMoreCredits:
                        dialog = gtk.MessageDialog(type=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, buttons=gtk.BUTTONS_YES_NO, message_format="{person:s} does not have enough credits - do you want to proceed?".format(person=person))
                        def on_response(dialog, response_id):
                            if response_id == gtk.RESPONSE_YES:
                                credits_left = settings.save_usage(person, extension_lenght, force=True)
                                do_start(credits_left)
                            dialog.destroy()
                        dialog.connect("response", on_response)
                        dialog.run()
                    return
                else:
                    self.log(
                        "Session for {name:s} expired, spawning new".format(
                            name=name,
                        )
                    )

        credits_left = 0
        try:
            credits_left = settings.save_usage(person, session['credits_cost'])
            self.log("Starting new session on {name:s} for person {person:s}, ends in {min:d} minutes".format(
                    name=name,
                    min=session['duration'],
                    person=person,
                )
            )
            do_start(credits_left)
        except settings.NoMoreCredits:
            dialog = gtk.MessageDialog(type=gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, buttons=gtk.BUTTONS_YES_NO, message_format="{person:s} does not have enough credits - do you want to proceed?".format(person=person))
            def on_response(dialog, response_id):
                if response_id == gtk.RESPONSE_YES:
                    credits_left = settings.save_usage(person, session['credits_cost'], force=True)
                    do_start(credits_left)
                dialog.destroy()
            dialog.connect("response", on_response)
            dialog.run()


    def kill_timeout(self, ip):
        deploy.sendfile("/tmp/lightdm.conf", "/etc/lightdm/autologin.conf", ips=[ip])
        deploy.deploy([REMOTE_STOP_KILL, REMOTE_STOP_WARN], ips=[ip])
    
    def kill_lightdm(self, ip):
        self.kill_timeout(ip)
        deploy.deploy(REMOTE_STOP_SESSION, ips=[ip])

    def start_lightdm(self, ip, session):
        f = open("/tmp/lightdm.conf", "w")
        f.write(LIGHTDM_CONF.format(username=session['username']))
        f.close()
        deploy.sendfile("/tmp/lightdm.conf", "/etc/lightdm/autologin.conf", ips=[ip])
        deploy.deploy(REMOTE_START_SESSION, ips=[ip])

    def start_timeout(self, ip, minutes, username):
        deploy.sendfile(WARNING_PY, "/tmp/warning.py", ips=[ip])
        warning_command = REMOTE_START_WARN.format(duration=(minutes-5 if minutes > 5 else 1), username=username)
        kill_command = REMOTE_START_KILL.format(duration=minutes)
        deploy.deploy([warning_command], ips=[ip])
        deploy.deploy([kill_command], ips=[ip])

    def get_widget(self, key):
        return self.glade.get_object(key)
    
    def on_delete_event(self, *args):
        """
        Display manager closed window.
        """
        self.win.destroy()
        gtk.main_quit()

    def on_destroy(self, *args):
        self.alive = False

    def on_start(self, *args):
        computer_no = self.glade.get_object("spinbuttonComputer").get_value()
        student_id = self.glade.get_object("entryStudentID").get_text()
        computer_no = int(computer_no)-1
        session_k = self.glade.get_object("comboboxSession").get_active_text()
        self.start_client(computer_no, session_k, student_id)
        time.sleep(2)

    def on_stop(self, *args):
        computer_no = self.glade.get_object("spinbuttonComputer").get_value()
        computer_no = int(computer_no)-1
        computer = settings.computers[computer_no]
        ip = computer[1]
        name = computer[0]
        self.log("Stopping session for {:s}".format(name))
        self.kill_timeout(ip)
        self.kill_lightdm(ip)
        if computer_no in self.started_clients:
            del self.started_clients[computer_no]
        time.sleep(2)
    
    def on_student_id_change(self, *args):
        if self.glade.get_object("entryStudentID").get_text():
            self.glade.get_object("buttonStart").set_sensitive(True)
        else:
            self.glade.get_object("buttonStart").set_sensitive(False)
    
    def log(self, msg):
        now = datetime.now()
        b = self.get_widget('textbuffer_log')
        msg_formatted = "[%s] %s\n" % (now.strftime("%H:%M"), msg)
        b.insert(b.get_end_iter(), msg_formatted)
        settings.logfile.write(msg_formatted)
        settings.logfile.flush()
    
    
if __name__ == '__main__':
    
    mainwindow = MainWindow()
    gtk.main()
    
    
    
