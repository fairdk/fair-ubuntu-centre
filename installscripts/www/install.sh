#!/bin/bash

# Here we set up the web server, and the directories that it depends on.

# Include variables defined externally

if [ -n "${SCRIPT_ROOT}" ]; then

        echo "Globals already defined"
else
        SCRIPT="`readlink -e $0`"
        SCRIPTPATH="`dirname $SCRIPT`"
        echo "Including global variables"
        export SCRIPT_ROOT=$SCRIPTPATH/..
        . $SCRIPTPATH/../config/default_cfg.sh
fi

WWW_SCRIPT_ROOT=$SCRIPT_ROOT/www

echo "---------------------------------------"
echo "Installing apache2 http server         "
echo "---------------------------------------"

apt-get install -y -q apache2

# Modules for apache
apt-get install -y -q libapache2-mod-wsgi

echo "---------------------------------------"
echo "Setting up local web server"
echo "---------------------------------------"

if [ ! -f /var/www/ubuntu/ubuntu ]
then
	ln -s /var/www/ubuntu/ /var/www/ubuntu/ubuntu
fi

if [ ! -d /var/www/ubuntu ]
then
	echo "Creating links for our repository"
	ln -s ${FAIR_ARCHIVE_PATH}/ubuntu /var/www/ubuntu
	ln -s /var/www/ubuntu/pool /var/www/pool
fi

echo "Copying Kickstart configuration file"
cp ${WWW_SCRIPT_ROOT}/ks*.cfg /var/www/
cp ${WWW_SCRIPT_ROOT}/edubuntu.seed /var/www/

echo "Installing default index.html"
cp ${WWW_SCRIPT_ROOT}/index.html /var/www

echo "Copying intranet"
if [ -f /var/www/intranet ]; then rm /var/www/intranet; fi
mkdir -p /var/www/intranet
cp -rf ${WWW_SCRIPT_ROOT}/intranet/* /var/www/intranet
chown -R root.root /var/www/intranet
chmod -R o+r /var/www/intranet
chmod -R o+X /var/www/intranet

echo "Creating virtual hosts for the repository and the intranet..."
cat ${WWW_SCRIPT_ROOT}/etc.apache2.sites-available.repo > /etc/apache2/sites-available/repo
cat ${WWW_SCRIPT_ROOT}/etc.apache2.sites-available.intranet > /etc/apache2/sites-available/intranet
a2ensite repo
a2ensite intranet

echo "---------------------------------------"
echo "Copying Wikipedia files                "
echo "---------------------------------------"

echo "Copying document root into /var/www/wiki"

if [ ! -d /var/www/wiki ]
then
	cd /var/www
	tar xvfz ${FAIR_ARCHIVE_PATH}/data/mediawiki.tar.gz
	cd -
	mv /var/www/mediawiki /var/www/wiki/
	ln -s ${FAIR_ARCHIVE_PATH}/data/wikipedia_media/results/ /var/www/wiki/images
	mkdir -p /var/www/wiki/images/thumb
	mkdir -p /var/www/wiki/images/archive
	mkdir -p /var/www/wiki/images/temp
	chmod 777 /var/www/wiki/images/thumb 
	chmod 777 /var/www/wiki/images/archive
	chmod 777 /var/www/wiki/images/temp
fi

echo "Copying configuration file LocalSettings.php into /var/www/wiki/"
cat ${WWW_SCRIPT_ROOT}/wikipedia.LocalSettings.php > /var/www/wiki/LocalSettings.php

echo "Creating virtual host"
cat ${WWW_SCRIPT_ROOT}/etc.apache2.sites-available.wikipedia > /etc/apache2/sites-available/wikipedia
a2ensite wikipedia

/etc/init.d/apache2 reload

echo "---------------------------------------"
echo "Khan Academy"
echo "---------------------------------------"

cat ${WWW_SCRIPT_ROOT}/etc.apache2.sites-available.khan > /etc/apache2/sites-available/khan
a2ensite khan


echo "---------------------------------------"
echo "Project Gutenberg"
echo "---------------------------------------"

if [ ! -d /var/www/gutenberg ]
then
        echo "Creating links for Project Gutenberg"
        ln -s ${FAIR_ARCHIVE_PATH}/data/project_gutenberg /var/www/gutenberg
else
	echo "Project Gutenberg already present"
fi

echo "---------------------------------------"
echo "Movies"
echo "---------------------------------------"

if [ ! -d /var/www/movies ]
then
        echo "Creating links for Movies"
	chmod -R o+r ${FAIR_ARCHIVE_PATH}/data/movies
	chmod -R o+X ${FAIR_ARCHIVE_PATH}/data/movies
        ln -s ${FAIR_ARCHIVE_PATH}/data/movies /var/www/movies
else
	echo "Movies directory already symlinked"
fi

echo "---------------------------------------"
echo "Ebooks"
echo "---------------------------------------"


if [ ! -d /var/www/ebooks ]
then
        echo "Creating links for ebooks"
	chmod -R o+r ${FAIR_ARCHIVE_PATH}/data/ebooks
	chmod -R o+X ${FAIR_ARCHIVE_PATH}/data/ebooks
        ln -s ${FAIR_ARCHIVE_PATH}/data/ebooks /var/www/ebooks
else
	echo "Ebooks directory already symlinked"
fi

echo "---------------------------------------"
echo "Camara"
echo "---------------------------------------"


if [ ! -d /var/www/camara ]
then
        echo "Creating links for Camara"
	chmod -R o+r ${FAIR_ARCHIVE_PATH}/data/camara
	chmod -R o+X ${FAIR_ARCHIVE_PATH}/data/camara
        ln -s ${FAIR_ARCHIVE_PATH}/data/camara /var/www/camara
else
	echo "Camara directory already symlinked"
fi

echo "---------------------------------------"
echo "Distro folder (iso images of other linux)"
echo "---------------------------------------"


if [ ! -d /var/www/distros ]
then
        echo "Creating links for linux distros"
	chmod -R o+r ${FAIR_ARCHIVE_PATH}/data/distros
	chmod -R o+X ${FAIR_ARCHIVE_PATH}/data/distros
        ln -s ${FAIR_ARCHIVE_PATH}/data/distros /var/www/distros
else
	echo "Linux distros directory already symlinked"
fi

