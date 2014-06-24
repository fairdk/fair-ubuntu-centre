#!/bin/bash

sudo apt-get -q -y install python-m2crypto

function sedeasy {
  sed -i "s/$(echo $1 | sed -e 's/\([[\/.*]\|\]\)/\\&/g')/$(echo $2 | sed -e 's/[\/&]/\\&/g')/g" $3
}

echo "---------------------------------------"
echo "Khan Academy"
echo "---------------------------------------"

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.kalite.conf > /etc/apache2/sites-available/kalite.conf

sedeasy "{{ FAIR_ARCHIVE_PATH }}" "$FAIR_ARCHIVE_PATH" /etc/apache2/sites-available/kalite.conf

a2ensite kalite

chmod -R 777 $FAIR_ARCHIVE_PATH/data/ka-lite/kalite/database

service apache2 reload

