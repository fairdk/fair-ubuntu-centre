#!/bin/bash

if [ ! -d $FAIR_DRIVE_MOUNTPOINT/data/ka-lite ]
then
	echo 'Echo "KA Lite not found"'
	return
fi

sudo apt-get -q -y install python-m2crypto

echo "---------------------------------------"
echo "Khan Academy"
echo "---------------------------------------"

echo "Copying in the .kalite data directory"
if [ ! -d /home/kalite ]
then
	echo "Creating a kalite user"
	useradd -m -U kalite
fi
tar xvz -f $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/kalite_home.tar.gz -C /home/kalite
chown -R kalite /home/kalite/.kalite
chmod -R o+wX /home/kalite/.kalite

echo "Installing KA Lite deb pkg"
echo "ka-lite ka-lite/init select false" | debconf-set-selections
# The * is because some drives may contain 0.17.0 and some 0.17.4
DEBIAN_FRONTEND=noninteractive dpkg -i $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/ka-lite_0.17*.deb

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.kalite.conf > /etc/apache2/sites-available/kalite.conf
cat ${FAIR_INSTALL_DATA}/ka-lite.wsgi > $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/ka-lite.wsgi

sedeasy "{{ FAIR_DRIVE_MOUNTPOINT }}" "$FAIR_DRIVE_MOUNTPOINT" /etc/apache2/sites-available/kalite.conf

a2ensite kalite

chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/content/assessment
chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/content/locale
chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/content/srt

service apache2 reload

