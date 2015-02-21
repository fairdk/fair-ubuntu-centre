#!/bin/bash

echo "---------------------------------------"
echo "Installing intranet                    "
echo "---------------------------------------"

apt-get install python-virtualenv libapache2-mod-wsgi -q -y

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.intranet.conf > /etc/apache2/sites-available/intranet.conf

echo "Copying intranet files and virtualenv"
mkdir -p /var/www/intranet
cp -R ${FAIR_INSTALL_DATA}/intranet/fairintranet /var/www/intranet/
cp -R ${FAIR_INSTALL_DATA}/intranet/virtualenv.tar.gz /var/www/intranet/

echo "Unpacking virtualenv"
cd /var/www/intranet
tar xfz virtualenv.tar.gz

# For file uploads
chmod -R 777 /var/www/intranet/fairintranet/media/
# Needed for populating CACHE
chmod -R 777 /var/www/intranet/fairintranet/static/

chown -R www-data.www-data /var/www/intranet/fairintranet/

# Run Django management scripts
source /var/www/intranet/virtualenv/bin/activate
python /var/www/intranet/fairintranet/manage.py set_site_name
python /var/www/intranet/fairintranet/manage.py collectstatic --noinput
deactivate

echo "Enabling intranet"
a2ensite intranet

echo "Reloading apache2"
service apache2 reload

echo "Symlinking resources to the main server root"
rm -f /var/www/html/movies
rm -f /var/www/html/ebooks
ln -s /media/FAIR/data/movies /var/www/html/movies
ln -s /media/FAIR/data/ebooks /var/www/html/ebooks
