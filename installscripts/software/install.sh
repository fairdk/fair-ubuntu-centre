#!/bin/bash

# Install config files in the ETC dir

if [ -n "${SCRIPT_ROOT}" ]; then
        echo "Globals already defined"
else
        SCRIPT="`readlink -e $0`"
        SCRIPTPATH="`dirname $SCRIPT`"
        echo "Including global variables"
        export SCRIPT_ROOT=$SCRIPTPATH/..
        . $SCRIPTPATH/../config/default_cfg.sh
fi

INSTALL_SCRIPT_ROOT=$SCRIPT_ROOT/software

echo "---------------------------------------"
echo "Putting external drive in /etc/fstab"
echo "---------------------------------------"

if (($USE_USB_DISK==1))
then

	if ! grep "${FAIR_ARCHIVE_PATH}" /etc/fstab -q
	then
		FAIR_MOUNT_PARTITION=`mount |grep FAIR|sed 's/\/dev\/\(....\)\ .*/\1/'`
		FAIR_PARTITION_UUID=`ls -l /dev/disk/by-uuid/ | grep $FAIR_MOUNT_PARTITION | sed 's/.* \([^ ]*\) -> .*/\1/'`
		echo "No entry in /etc/fstab... Will now create one for /dev/sdb1"
		echo "UUID=$FAIR_PARTITION_UUID	${FAIR_ARCHIVE_PATH}	ext4	 errors=remount-ro,noatime,async 0 0" >> /etc/fstab
		mkdir -p ${FAIR_ARCHIVE_PATH}
		mount -a
	else
		echo "Already present!"
	fi
else
	echo "USB disk NOT added to FSTAB" 
fi


echo "---------------------------------------"
echo "Remove unecessary software"
echo "---------------------------------------"

# Remove avahi-daemon, not needed and causes problems on different networking setups
apt-get -y -q remove libreoffice-* rhythmbox ubuntuone-* apport evince gnome-orca gwibber thunderbird software-center


echo "---------------------------------------"
echo "Configuring the network on eth0"
echo "---------------------------------------"

# We get rid of the automatic network configuration tool to do things ourself
#apt-get remove -y -q dnsmasq-base network-manager network-manager-gnome

cat ${INSTALL_SCRIPT_ROOT}/etc.network.interfaces > /etc/network/interfaces
/etc/init.d/networking restart

echo "Overwriting /etc/hosts"
cat ${INSTALL_SCRIPT_ROOT}/etc.hosts > /etc/hosts

echo "fair-server" > /etc/hostname

echo "---------------------------------------"
echo "Installing rc.local                    "
echo "---------------------------------------"
# This script is run every time the system reboots.
cat ${INSTALL_SCRIPT_ROOT}/etc.rc.local > /etc/rc.local



echo "---------------------------------------"
echo "Configuring apt repository             "
echo "---------------------------------------"

mkdir -p /var/www/
if [ ! -d /var/www/ubuntu ]
then
        echo "Creating links for our repository"
        ln -s ${FAIR_ARCHIVE_PATH}/ubuntu /var/www/ubuntu
        ln -s /var/www/ubuntu/pool /var/www/pool
fi

cat ${INSTALL_SCRIPT_ROOT}/sources.list > /etc/apt/sources.list

# We run "configure" to start with because half-installed packages can cause apt-get to fail, and this prevents that...
sudo dpkg --configure -a

# Use the local repository...
apt-get update

sudo dpkg --configure -a


echo "---------------------------------------"
echo "Installing dnsmasq DHCP & DNS server   "
echo "---------------------------------------"

# The network manager conflicts with the dnsmasq package, so if we want to keep it (and I do for development) we have to reconfigure it
# see also: http://sokratisg.net/2012/03/31/ubuntu-precise-12-04-get-rid-of-nms-dnsmasq-and-setup-your-own/
cat ${INSTALL_SCRIPT_ROOT}/etc.NetworkManager.conf > /etc/NetworkManager/NetworkManager.conf
restart network-manager

apt-get install -y -q dnsmasq

echo "Creating configuration file /etc/dnsmasq.d/fair"
cat ${INSTALL_SCRIPT_ROOT}/etc.dnsmasq.d.fair > /etc/dnsmasq.d/fair

/etc/init.d/dnsmasq restart


echo "---------------------------------------"
echo "Installing NTP time server             "
echo "---------------------------------------"
# Deleting old config prevents prompt when installing ntp.
rm /etc/ntp.conf

apt-get install -y -q ntp
echo "Copying NTP configuration..."
cat ${INSTALL_SCRIPT_ROOT}/etc.ntp.conf > /etc/ntp.conf
/etc/init.d/ntp restart



echo "---------------------------------------"
echo "Installing MySQL and PHP               "
echo "---------------------------------------"

# PJD: TODO Remove prompt to set password
# Maybe it works now...
apt-get install -y -q mysql-server php5 php5-mysql

# Move mysql
# This is in case MySQL was already installed..
# so we backup the old database
if [ ! -d /var/lib/mysql_old ]
then
	mv /var/lib/mysql /var/lib/mysql_old
else
	rm /var/lib/mysql
fi

echo "Linking MySQL data dir to /var/lib/mysql"
ln -s ${FAIR_ARCHIVE_PATH}/data/mysql /var/lib/mysql

echo "Setting owner to mysql"
chown -R mysql.mysql ${FAIR_ARCHIVE_PATH}/data/mysql

echo "Installing apparmor configuration"
cat ${INSTALL_SCRIPT_ROOT}/etc.apparmor.d.usr.sbin.mysqld > /etc/apparmor.d/disable/usr.sbin.mysqld
/etc/init.d/apparmor reload

echo "Creating new /etc/mysql/my.cnf"
cp ${INSTALL_SCRIPT_ROOT}/etc.mysql.my.cnf /etc/mysql/my.cnf

echo "Restarting MySQL"
stop mysql
start mysql


echo "---------------------------------------"
echo "Installing ImageMagick                 "
echo "---------------------------------------"

apt-get install -y -q imagemagick


echo "---------------------------------------"
echo "Installing extra optional stuff        "
echo "---------------------------------------"

echo "Installing ping_clients.py"

cp ${INSTALL_SCRIPT_ROOT}/ping_clients/ping_clients.py /usr/local/sbin
cp ${INSTALL_SCRIPT_ROOT}/ping_clients/ping_clients /etc/init.d
chmod +x /etc/init.d/ping_clients
update-rc.d -f ping_clients defaults remove
update-rc.d ping_clients defaults

apt-get install -y -q openssh-server
apt-get install -y -q x11vnc
cp etc.init.d.x11vnc /etc/init.d/x11vnc
chmod +x /etc/init.d/x11vnc
update-rc.d x11vnc start 99 4 5 .

# Done
exit 0
