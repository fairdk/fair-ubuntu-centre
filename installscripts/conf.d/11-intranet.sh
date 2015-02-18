#!/bin/bash

echo "---------------------------------------"
echo "Installing intranet                    "
echo "---------------------------------------"

apt-get install python-virtualenv libapache2-mod-wsgi -q -y

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.intranet.conf > /etc/apache2/sites-available/intranet.conf

echo "Copying intranet files and virtualenv"
cp -R ${FAIR_INSTALL_DATA}/intranet /var/www/

# For file uploads
chmod 777 /var/www/intranet/fairintranet/media/
# Needed for populating CACHE
chmod 777 /var/www/intranet/fairintranet/static/

# Run Django management scripts
source /var/www/intranet/virtualenv/bin/activate
python /var/www/intranet/fairintranet/manage.py set_site_name
python /var/www/intranet/fairintranet/manage.py collectstatic --noinput
deactivate

echo "Enabling intranet"
a2ensite intranet

echo "Reloading apache2"
service apache2 reload
