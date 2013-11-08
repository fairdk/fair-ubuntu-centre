#!/bin/bash

USAGE="Usage: sync_to_dir.sh <DIR>\nDo not add trailing slash '/' to DIR."
if [ "$1" == "-h" ]
then
	echo $USAGE
	exit
fi

syncto="$1"

if [ "$syncto" == "" ]
then
	echo "Not set, using /root/installscripts"
	syncto="/root/installscripts"
fi
SCRIPT="`readlink -e $0`"
SCRIPTPATH="`dirname $SCRIPT`"

echo "Delete files that do not exist in $SCRIPTPATH yet exists in $syncto ?"
select yn in "Yes" "No"; do
    case $yn in
        [Yy]* ) 
		rsync -avu --delete --exclude "postinstall.tar.gz" --exclude "server_id_rsa.pub" $SCRIPTPATH/ $syncto
                break;;
        [Nn]* ) 
		rsync -avu $SCRIPTPATH/ $syncto
		break;;
    esac
done

echo "Do you wish to sync $syncto/ -> $SCRIPTPATH/ ?"
select yn in "Yes" "No"; do
    case $yn in
        [Yy]* )
		rsync -avu --delete  --exclude "postinstall.tar.gz" --exclude "server_id_rsa.pub" $syncto/ $SCRIPTPATH
		break;;
        [Nn]* ) break;;
    esac
done
