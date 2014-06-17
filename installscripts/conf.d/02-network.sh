echo "---------------------------------------"
echo "Configuring the network on eth0"
echo "---------------------------------------"

# We get rid of the automatic network configuration tool to do things ourself
#apt-get remove -y -q dnsmasq-base network-manager network-manager-gnome

cat ${FAIR_INSTALL_DATA}/etc.network.interfaces > /etc/network/interfaces
ifdown -a
ifup -a

echo "Altering /etc/hosts"

if ! grep "$FAIR_SERVER_HOSTNAME" /etc/hosts -q
then
	echo "127.0.0.1 $FAIR_SERVER_HOSTNAME" >> /etc/hosts
fi

if ! grep "192.168.10.1" /etc/hosts -q
then
	echo 192.168.10.1 intranet intranet.fair fair repo.fair wikipedia.fair repo dvd.fair khan.fair khan >> /etc/hosts
fi

if ! grep "archive.canonical.com" /etc/hosts -q
then
	echo 192.168.10.1 archive.canonical.com >> /etc/hosts
fi



echo "$FAIR_SERVER_HOSTNAME" > /etc/hostname
hostname "$FAIR_SERVER_HOSTNAME"

echo "---------------------------------------"
echo "Installing dnsmasq DHCP & DNS server   "
echo "---------------------------------------"

# The network manager conflicts with the dnsmasq package, so if we want to keep it (and I do for development) we have to reconfigure it
# see also: http://sokratisg.net/2012/03/31/ubuntu-precise-12-04-get-rid-of-nms-dnsmasq-and-setup-your-own/
cat ${FAIR_INSTALL_DATA}/etc.NetworkManager.conf > /etc/NetworkManager/NetworkManager.conf

# remove resolvconf so it doesn't write 127.0.0.1 in /etc/resolv.conf

apt-get remove -y -q resolvconf

restart network-manager

apt-get install -y -q dnsmasq

echo "Creating configuration file /etc/dnsmasq.d/fair"
cat ${FAIR_INSTALL_DATA}/etc.dnsmasq.d.fair > /etc/dnsmasq.d/fair

/etc/init.d/dnsmasq restart


echo "---------------------------------------"
echo "Installing NTP time server             "
echo "---------------------------------------"
# Deleting old config prevents prompt when installing ntp.
rm /etc/ntp.conf

apt-get install -y -q ntp
echo "Copying NTP configuration..."
cat ${FAIR_INSTALL_DATA}/etc.ntp.conf > /etc/ntp.conf
/etc/init.d/ntp restart


