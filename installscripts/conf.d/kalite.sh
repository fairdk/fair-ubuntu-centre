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
cd /home/fair
tar xvfz $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/kalite_home.tar.gz
chown -R fair.fair .kalite
cd -

echo "Installing KA Lite deb pkg"
echo "ka-lite ka-lite/init select false" | debconf-set-selections
DEBIAN_FRONTEND=noninteractive dpkg -i $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/ka-lite_0.17.0-0ubuntu1_all.deb

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.kalite.conf > /etc/apache2/sites-available/kalite.conf

# Patch errors in ka lite imports
echo "" > $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/kalite/testing/__init__.py
echo "" > $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/python-packages/fle_utils/testing/__init__.py

sedeasy "{{ FAIR_DRIVE_MOUNTPOINT }}" "$FAIR_DRIVE_MOUNTPOINT" /etc/apache2/sites-available/kalite.conf

a2ensite kalite

chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/content/assessment
chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/content/locale
chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/content/srt

service apache2 reload

