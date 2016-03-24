#!/bin/bash

echo "---------------------------------------"
echo "Installing intranet                    "
echo "---------------------------------------"

INTRANET_ROOT=/var/www/intranet

apt-get install python-virtualenv libapache2-mod-wsgi -q -y

cat ${FAIR_INSTALL_DATA}/etc.apache2.sites-available.intranet.conf > /etc/apache2/sites-available/intranet.conf

echo "Copying intranet files and virtualenv"
mkdir -p $INTRANET_ROOT

# Leaving migration files behind can be dangerous so just delete everything
# for now...
rm -rf $INTRANET_ROOT/fairintranet

# Creating the intranet
cp -R ${FAIR_INSTALL_DATA}/intranet/fairintranet $INTRANET_ROOT/

# Copying media
cp -Ru ${FAIR_INSTALL_DATA}/intranet/media $INTRANET_ROOT/

echo "Copying virtualenv"
$VIRTUAL_ENV=${FAIR_INSTALL_DATA}/intranet/virtualenv
if [ -d "${VIRTUAL_ENV}" ]
then
	rm -rf $VIRTUAL_ENV
fi
cp --archive ${FAIR_INSTALL_DATA}/intranet/virtualenv $INTRANET_ROOT/

# Activate virtualenv
source $INTRANET_ROOT/virtualenv/bin/activate

deploy_new=1

if [ -f "$INTRANET_ROOT/db.sqlite3" ]
then
	echo "A database file for the intranet already exists"
	read -p "Do you wish to keep it? [Y/n]" yn
	if [ ! "$yn" ] || [ "$yn" == "Y" ] || [ "$yn" == "y" ]
	then
		deploy_new=0
	else
		deploy_new=1
	fi
fi

# Remove old link, it will be recreated anyways
rm -f $INTRANET_ROOT/fairintranet/db.sqlite3

if [ $deploy_new -eq 1 ]
then
	echo "No database file, deploying a new one"
	cp ${FAIR_INSTALL_DATA}/intranet/db.sqlite3 $INTRANET_ROOT/db.sqlite3
        ln -s $INTRANET_ROOT/db.sqlite3 $INTRANET_ROOT/fairintranet/db.sqlite3
	python $INTRANET_ROOT/fairintranet/manage.py install_site
	echo "Creating thumbnails for EBook resources"
	python $INTRANET_ROOT/fairintranet/manage.py create_thumbnails ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks/
	echo "Automatically adding EBook resources"
	python $INTRANET_ROOT/fairintranet/manage.py import_resource_folder ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks/Camara 5 --author="Camara"
	python $INTRANET_ROOT/fairintranet/manage.py import_resource_folder ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks/NICE 94 --author="National Initiative for Civic Education"
else
	echo "Running possible migrations on the database..."
        ln -s $INTRANET_ROOT/db.sqlite3 $INTRANET_ROOT/fairintranet/db.sqlite3
	python $INTRANET_ROOT/fairintranet/manage.py migrate
fi

# Run Django management scripts
echo "Populating static files for intranet"
python $INTRANET_ROOT/fairintranet/manage.py collectstatic --noinput > /dev/null

deactivate

# For file uploads
chmod -R 777 $INTRANET_ROOT/media/
# Needed for populating CACHE
chmod -R 777 $INTRANET_ROOT/fairintranet/static/

chown -R www-data.www-data $INTRANET_ROOT/

echo "Enabling intranet"
a2ensite intranet

echo "Reloading apache2"
service apache2 reload

echo "Symlinking resources to the main server root"
rm -f /var/www/html/movies
rm -f /var/www/html/ebooks
ln -s ${FAIR_DRIVE_MOUNTPOINT}/data/movies /var/www/html/movies
ln -s ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks /var/www/html/ebooks
chmod -R o+r ${FAIR_DRIVE_MOUNTPOINT}/data/movies
chmod -R o+X ${FAIR_DRIVE_MOUNTPOINT}/data/movies
chmod -R o+r ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks
chmod -R o+X ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks

if [ -d ${FAIR_DRIVE_MOUNTPOINT}/data/movies/why_democracy/ ]
then
	echo "Patching up why democracy .pls files"
	sed -i 's/var\/why\_democracy/var\/movies\/why_democracy/g' ${FAIR_DRIVE_MOUNTPOINT}/data/movies/why_democracy/*pls
fi
