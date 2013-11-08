#!/bin/sh

cp create_homes.sh /etc/init.d/create_homes
chmod 755 /etc/init.d/create_homes

cp student.gconf.lst /root/

rm -Rf /root/student
rm -Rf /root/teacher
cp -R student /root/
cp -R teacher /root/
update-rc.d -f create_homes remove
update-rc.d create_homes defaults

