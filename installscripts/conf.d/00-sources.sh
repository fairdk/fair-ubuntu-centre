#!/bin/bash

echo "---------------------------------------"
echo "Putting external drive in /etc/fstab"
echo "---------------------------------------"

if (($USE_USB_DISK==1))
then

	if ! grep "${FAIR_ARCHIVE_PATH}" /etc/fstab -q
	then
		FAIR_MOUNT_PARTITION=`mount |grep FAIR|sed 's/\/dev\/\(....\)\ .*/\1/'`
		FAIR_PARTITION_UUID=`ls -l /dev/disk/by-uuid/ | grep $FAIR_MOUNT_PARTITION | sed 's/.* \([^ ]*\) -> .*/\1/'`
		if [[ "$FAIR_PARTITION_UUID" != "" ]]
		then
			echo "No entry in /etc/fstab... Will now create one for /dev/sdb1"
			echo "UUID=$FAIR_PARTITION_UUID	${FAIR_ARCHIVE_PATH}	ext4	 errors=remount-ro,noatime,async 0 0" >> /etc/fstab
			mkdir -p ${FAIR_ARCHIVE_PATH}
			mount -a
		else
			echo "No UUID for FAIR archive path, assuming it's a directory"
		fi
	else
		echo "Already present!"
	fi
else
	echo "USB disk NOT added to FSTAB" 
fi

