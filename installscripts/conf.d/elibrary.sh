echo "---------------------------------------"
echo "Ebooks"
echo "---------------------------------------"


if [ ! -d /var/www/ebooks ]
then
        echo "Creating links for ebooks"
	chmod -R o+r ${FAIR_ARCHIVE_PATH}/data/ebooks
	chmod -R o+X ${FAIR_ARCHIVE_PATH}/data/ebooks
        ln -s ${FAIR_ARCHIVE_PATH}/data/ebooks /var/www/ebooks
else
	echo "Ebooks directory already symlinked"
fi


