echo "---------------------------------------"
echo "Copying TFTP root directory            "
echo "---------------------------------------"

echo "Copying tftp root directory... can take up to a couple of minutes..."

# Danger: DNSMasq has already been started, and counts on this TFTP directory being present (that's why the directory was created in network.sh)
rm -Rf /var/tftp
mkdir /var/tftp

# The TFTP server is used to boot the clients from the network.  The DHCP server tells the clients to fetch their operating system over TFTP.
# The contents of the server are packaged in two parts, a compressed archive from http://cdimage.ubuntu.com/netboot/, and a (FAIR custom made) configuration file that is copied on top. 

if [ -f "${FAIR_ARCHIVE_PATH}/ubuntu/netboot.tar.gz" ]
then
	tar xvfz "${FAIR_ARCHIVE_PATH}/ubuntu/netboot.tar.gz" --directory /var/tftp/
else
	tar xvfz "$FAIR_INSTALL_DATA/tftp/netboot.tar.gz" --directory /var/tftp/
fi
cp $FAIR_INSTALL_DATA/tftp/txt.cfg /var/tftp/ubuntu-installer/i386/boot-screens/

