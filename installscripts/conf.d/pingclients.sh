echo "---------------------------------------"
echo "Ping clients (automatically turn off server) "
echo "---------------------------------------"

echo "Installing ping_clients.py"

cp ${FAIR_INSTALL_DATA}/ping_clients/ping_clients.py /usr/local/sbin
cp ${FAIR_INSTALL_DATA}/ping_clients/ping_clients /etc/init.d
chmod +x /etc/init.d/ping_clients
update-rc.d -f ping_clients defaults remove
update-rc.d ping_clients defaults

