#!/bin/bash

echo "---------------------------------------"
echo "Putting external drive in /etc/fstab"
echo "---------------------------------------"

if (("$USE_FAIR_DISK"==1))
then
	sedeasy_delete "${FAIR_DRIVE_MOUNTPOINT}" /etc/fstab
	echo "Removed ${FAIR_DRIVE_MOUNTPOINT} from fstab"
	# TODO: This should not be necessary anymore because above should delete
	# drive in all cases.
	if ! grep "${FAIR_DRIVE_MOUNTPOINT}" /etc/fstab -q
	then
		FAIR_MOUNT_PARTITION=`mount | grep FAIR | sed 's/\/dev\/\(....\)\ .*/\1/g'`
		FAIR_PARTITION_UUID=`ls -l /dev/disk/by-uuid/ | grep $FAIR_MOUNT_PARTITION | sed 's/.* \([^ ]*\) -> .*/\1/'`
		if [[ "$FAIR_PARTITION_UUID" == "" ]]
		then
			FAIR_PARTITION_UUID="/dev/$FAIR_MOUNT_PARTITION"
			echo "WARNING! No UUID found for partition, will use unreliable drive letter"
		else
			FAIR_PARTITION_UUID="UUID=${FAIR_PARTITION_UUID}"
		fi
		echo "No entry in /etc/fstab... Will now create one for ${FAIR_PARTITION_UUID}"
		echo "${FAIR_PARTITION_UUID}	${FAIR_DRIVE_MOUNTPOINT}	ext4	 errors=remount-ro,noatime,async 0 0" >> /etc/fstab
		mkdir -p ${FAIR_DRIVE_MOUNTPOINT}
		chmod 755 ${FAIR_DRIVE_MOUNTPOINT}
		mount -a
	else
		echo "Already present!"
	fi
else
	echo "FAIR disk NOT added to FSTAB" 
fi

