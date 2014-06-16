echo "---------------------------------------"
echo "Project Gutenberg"
echo "---------------------------------------"

if [ ! -d /var/www/gutenberg ]
then
        echo "Creating links for Project Gutenberg"
        ln -s ${FAIR_ARCHIVE_PATH}/data/project_gutenberg /var/www/gutenberg
else
	echo "Project Gutenberg already present"
fi


