#!/bin/bash

sudo apt-get -q -y install python-m2crypto

echo "---------------------------------------"
echo "Khan Academy"
echo "---------------------------------------"

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.kalite.conf > /etc/apache2/sites-available/kalite.conf

# Patch local_settings to use db based sessions
cat ${FAIR_INSTALL_DATA}/kalite_local_settings.py > $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/kalite/local_settings.py

# Patch errors in ka lite imports
echo "" > $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/kalite/testing/__init__.py
echo "" > $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/python-packages/fle_utils/testing/__init__.py

sedeasy "{{ FAIR_DRIVE_MOUNTPOINT }}" "$FAIR_DRIVE_MOUNTPOINT" /etc/apache2/sites-available/kalite.conf

a2ensite kalite

chmod -R 777 $FAIR_DRIVE_MOUNTPOINT/data/ka-lite/kalite/database

service apache2 reload

