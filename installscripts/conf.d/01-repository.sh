echo "---------------------------------------"
echo "Configuring apt repository             "
echo "---------------------------------------"

mkdir -p /var/www/html/

# Create the links to our Ubuntu repository if they don't already exist
if [ ! -L /var/www/html/ubuntu ]
then
        echo "Creating links for our repository"
        ln -s ${FAIR_DRIVE_MOUNTPOINT}/ubuntu /var/www/html/ubuntu
        ln -s /var/www/html/ubuntu/pool /var/www/html/pool
fi

# Configure the server to find software on the local Ubuntu repository
echo "deb file:///var/www/html/ubuntu trusty main restricted universe multiverse" > /etc/apt/sources.list

if [ -d ${FAIR_DRIVE_MOUNTPOINT}/ubuntu/dists/trusty-security ]
then
	echo "deb file:///var/www/html/ubuntu trusty-security main restricted universe multiverse" >> /etc/apt/sources.list
fi
if [ -d ${FAIR_DRIVE_MOUNTPOINT}/ubuntu/dists/trusty-updates ]
then
	echo "deb file:///var/www/html/ubuntu trusty-updates main restricted universe multiverse" >> /etc/apt/sources.list
fi

# We run "configure" to start with because half-installed packages can cause apt-get to fail, and this prevents that...
dpkg --configure -a

# Use the local repository to update the installation...
apt-get update

dpkg --configure -a

apt-get autoremove -y -q

# Make sure the server is fully upgraded
apt-get upgrade -y -q
