echo "---------------------------------------"
echo "Wikipedia Offline edition              "
echo "---------------------------------------"

echo "Copying mediawiki into /var/www/wiki"

if [ ! -d /var/www/wiki ]
then
	cd /var/www
	tar xvfz ${FAIR_ARCHIVE_PATH}/data/mediawiki.tar.gz
	cd -
	mv /var/www/mediawiki /var/www/wiki/
	ln -s ${FAIR_ARCHIVE_PATH}/data/wikipedia_media/results/ /var/www/wiki/images
	mkdir -p /var/www/wiki/images/thumb
	mkdir -p /var/www/wiki/images/archive
	mkdir -p /var/www/wiki/images/temp
	chmod 777 /var/www/wiki/images/thumb 
	chmod 777 /var/www/wiki/images/archive
	chmod 777 /var/www/wiki/images/temp
fi

echo "Copying configuration file LocalSettings.php into /var/www/wiki/"
cat ${WWW_SCRIPT_ROOT}/wikipedia.LocalSettings.php > /var/www/wiki/LocalSettings.php

echo "Creating virtual host"
cat ${WWW_SCRIPT_ROOT}/etc.apache2.sites-available.wikipedia > /etc/apache2/sites-available/wikipedia
a2ensite wikipedia

service apache2 reload


