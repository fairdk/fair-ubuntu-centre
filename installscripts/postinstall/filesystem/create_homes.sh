#! /bin/sh
### BEGIN INIT INFO
# Provides:          Reset home folders
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $local_fs $remote_fs $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Default-Stop:
# Short-Description: Run /etc/rc.local if it exist
### END INIT INFO


PATH=/sbin:/usr/sbin:/bin:/usr/bin

. /lib/init/vars.sh
. /lib/lsb/init-functions

do_start() {

	# Disable locks in gsettings
	gsettings set org.gnome.desktop.lockdown disable-lock-screen 'true'
	gsettings set org.gnome.desktop.screensaver lock-enabled 'false'

	# Remove all gconf stuff
	rm -Rf /home/student/.gconf
	rm -Rf /home/student/.gconfd

	rm -Rf /home/student/.config
	rm -Rf /home/student/.adobe
	rm -Rf /home/student/.gtk-bookmarks

	# Do not delete student Desktop in case of blackout
        #rm -rf /home/student/Desktop/*

	cd /root/postinstall
	cp -Rf student /home
	cp -Rf teacher /home

	# Gconf options for student
	su student -c "sh ~/.reset_gconf.sh"
	# Gconf options for teacher
	su teacher -c "sh ~/.reset_gconf.sh"

	rm -Rf /home/student/.mozilla
	rm -Rf /home/student/.openoffice.org
	rm -Rf /home/student/.nautilus
	rm -Rf /home/student/.gstreamer-0.10

	chmod 755 /home/student
	chown -R student.student /home/student

	cp -Rf teacher /home
	chmod 700 /home/teacher
	chown -R teacher.teacher /home/teacher

	rm -Rf /home/teacher/.mozilla

}

case "$1" in
    start)
	do_start
        ;;
    restart|reload|force-reload)
        echo "Error: argument '$1' not supported" >&2
        exit 3
        ;;
    stop)
        ;;
    *)
        echo "Usage: $0 start|stop" >&2
        exit 3
        ;;
esac
