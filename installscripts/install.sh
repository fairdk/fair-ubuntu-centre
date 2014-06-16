#!/bin/bash

# PJD: Important design consideration:  This script should be able to upgrade an existing server, therefore all operations must start by removing and old crap and ensuring a complete overwrite of the contents.  This feature can be especially handy when developing too :).  Could consider starting script with a warning WILL ERASE EXISTING INSTALLATION, ARE YOU SURE...

# Include variables defined externally
. ./config/default_cfg.sh

echo "---------------------------------------"
echo "Starting FAIR install"
echo "---------------------------------------"

# Check dependancies- permissions, and access to media drive 
if !(whoami | grep "root" -q)
then
	echo "Only root can run this!"
	echo ""
	echo "Run the program as root, ie.:"
	echo "sudo bash install.sh"
	exit 1
fi

if [ ! -d $FAIR_ARCHIVE_PATH ]
then
	echo "FAIR USB drive not detected in $FAIR_ARCHIVE_PATH"
	exit 1
fi

echo "---------------------------------------"
echo "Installing config files"
echo "---------------------------------------"

if [ ! "$1" = "" ]
then
	echo "Running $1"
	. "$FAIR_INSTALL_CONF_D/$1"
else
	for file in `ls "$FAIR_INSTALL_CONF_D" --hide *.disabled`
	do
		if [ -f "$FAIR_INSTALL_CONF_D/$file" ]; then
			skip=no
			case "${FAIR_CONF_D_SKIP[@]}" in  *"$file"*) skip=yes ;; esac
			[ skip=no ] && . "$FAIR_INSTALL_CONF_D/$file"
		fi
	done
fi


apt-get -y -q upgrade


echo "---------------------------------------"
echo "Adding local overlay                   "
echo "---------------------------------------"

./config/local.sh

echo "---------------------------------------"
echo "Creating client postinstall package    "
echo "---------------------------------------"
./postinstall/make_postinstall.sh
