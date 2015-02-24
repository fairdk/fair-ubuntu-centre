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

	# Re-add stuff from the skel
	cp -R /etc/skel/* /home/teacher/
	cp -R /etc/skel/* /home/student/
	# Hidden files, too, it will say some useless stuff about . and ..
	cp /etc/skel/.* /home/teacher/ 2>&1
	cp /etc/skel/.* /home/student/ 2>&1

	# Re-deploy whatever is here
	cd /root/postinstall
	cp -Rf student /home
	cp -Rf teacher /home

	chmod 755 /home/student
	chown -R student.student /home/student

	cp -Rf teacher /home
	chmod 700 /home/teacher
	chown -R teacher.teacher /home/teacher

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
