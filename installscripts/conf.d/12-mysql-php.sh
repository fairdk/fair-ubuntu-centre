# Disable temporarily because it was only used for Wikipedia wich is replace
# by Kiwix

exit 0

echo "---------------------------------------"
echo "Installing MySQL and PHP               "
echo "---------------------------------------"

# From http://www.microhowto.info/howto/perform_an_unattended_installation_of_a_debian_package.html
echo mysql-server-5.5 mysql-server/root_password password "$FAIR_MYSQL_PASSWORD" | debconf-set-selections
echo mysql-server-5.5 mysql-server/root_password_again password "$FAIR_MYSQL_PASSWORD" | debconf-set-selections
apt-get install -y -q mysql-server php5 php5-mysql

if [ -d "${FAIR_ARCHIVE_PATH}/data/mysql" ]
then
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
else
    echo "No mysql directory found in the FAIR archive."
fi

# PDO: Insert some comment here about why we want apparmor; I can't say for sure...
echo "Installing apparmor configuration"
cat ${FAIR_INSTALL_DATA}/etc.apparmor.d.usr.sbin.mysqld > /etc/apparmor.d/disable/usr.sbin.mysqld
/etc/init.d/apparmor reload

echo "Creating new /etc/mysql/my.cnf"
# PDO: What is different in the new config, compared to the default? (comments could be added in the cnf file itself, instead of here...)
cp ${FAIR_INSTALL_DATA}/etc.mysql.my.cnf /etc/mysql/my.cnf

echo "Restarting MySQL"
service mysql restart

# Reinstall database for phpmyadmin?
echo phpmyadmin phpmyadmin/dbconfig-install boolean true | debconf-set-selections
echo phpmyadmin phpmyadmin/dbconfig-reinstall boolean true | debconf-set-selections
echo phpmyadmin phpmyadmin/mysql/admin-pass password $FAIR_MYSQL_PASSWORD | debconf-set-selections
echo phpmyadmin phpmyadmin/dbconfig-upgrade boolean true | debconf-set-selections
echo phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2 | debconf-set-selections

apt-get install -y -q phpmyadmin

