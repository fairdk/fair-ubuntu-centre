#!/bin/bash

# Install config files in the ETC dir

echo "---------------------------------------"
echo "Remove unecessary software (that comes with Ubuntu by default)"
echo "---------------------------------------"

# Remove avahi-daemon, not needed and causes problems on different networking setups
apt-get -y -q remove apport gnome-orca gwibber zeitgeist unity-webapps-common


echo "---------------------------------------"
echo "Installing rc.local                    "
echo "---------------------------------------"
# This script is run every time the system reboots.
cat ${FAIR_INSTALL_DATA}/etc.rc.local > /etc/rc.local



echo "---------------------------------------"
echo "Installing more usefull utilities (such as ImageMagick and an SSH Server)"
echo "---------------------------------------"

apt-get install -y -q imagemagick
apt-get install -y -q openssh-server
