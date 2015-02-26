#!/bin/bash

if [ ! -d $FAIR_DRIVE_MOUNTPOINT/data/kiwix ]
then
        echo 'Echo "Kiwix not found"'
        return
fi

echo "---------------------------------------"
echo "Kiwix (digital library)"
echo "---------------------------------------"

cp -Ruf $FAIR_DRIVE_MOUNTPOINT/data/kiwix/kiwix /opt/

cat ${FAIR_INSTALL_DATA}/etc.init.d.kiwix > /etc/init.d/kiwix

sedeasy "{{ FAIR_DRIVE_MOUNTPOINT }}" "$FAIR_DRIVE_MOUNTPOINT" /etc/init.d/kiwix

chmod +x /etc/init.d/kiwix

update-rc.d -f kiwix remove
update-rc.d kiwix defaults

/etc/init.d/kiwix start
