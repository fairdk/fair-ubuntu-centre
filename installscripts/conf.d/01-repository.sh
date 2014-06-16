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

cat ${FAIR_INSTALL_DATA}/sources.list > /etc/apt/sources.list

# We run "configure" to start with because half-installed packages can cause apt-get to fail, and this prevents that...
dpkg --configure -a

# Use the local repository...
apt-get update

dpkg --configure -a

apt-get autoremove -y -q
