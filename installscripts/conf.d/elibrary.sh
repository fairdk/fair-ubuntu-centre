echo "---------------------------------------"
echo "Ebooks"
echo "---------------------------------------"


if [ ! -d /var/www/html/ebooks ] && [ -d ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks ]
then
        echo "Creating links for ebooks"
	chmod -R o+r ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks
	chmod -R o+X ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks
        ln -s ${FAIR_DRIVE_MOUNTPOINT}/data/ebooks /var/www/html/ebooks
else
	echo "Ebooks directory already symlinked"
fi


