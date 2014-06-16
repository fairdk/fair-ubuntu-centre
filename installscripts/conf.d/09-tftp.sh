echo "---------------------------------------"
echo "Copying TFTP root directory            "
echo "---------------------------------------"

echo "Copying tftp root directory... can take up to a couple of minutes..."

rm -Rf /var/tftp
mkdir /var/tftp
tar xvfz $FAIR_INSTALL_DATA/tftp/netboot.tar.gz --directory /var/tftp/
cp $FAIR_INSTALL_DATA/tftp/txt.cfg /var/tftp/ubuntu-installer/i386/boot-screens/
