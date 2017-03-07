#!/bin/bash

# Enable tracebacks
set -eu

# Include variables defined externally

# This sets $SCRIPT_ROOT to a default if unset
SCRIPT="`readlink -e $0`"
: ${SCRIPT_ROOT:="`dirname $SCRIPT`"}

. $SCRIPT_ROOT/traceback.sh

POSTINSTALL_SCRIPT_ROOT=$SCRIPT_ROOT/postinstall
PI_FILESYSTEM_ROOT=${POSTINSTALL_SCRIPT_ROOT}/filesystem

# Main script to be run on clients
chmod +x ${PI_FILESYSTEM_ROOT}/postinstall.sh

if [ ! -d /root/.ssh ]
then
        mkdir /root/.ssh
        chmod 700 /root/.ssh
fi
if [ ! -f /root/.ssh/id_rsa ]
then
	echo "Making SSH keys for server admin"
        ssh-keygen -N "" -q -f "/root/.ssh/id_rsa"
fi
cp /root/.ssh/id_rsa.pub ${PI_FILESYSTEM_ROOT}/server_id_rsa.pub

# Allow site-specific custom files to be included.
#rm -Rf ${PI_FILESYSTEM_ROOT}/local
mkdir -p ${PI_FILESYSTEM_ROOT}/local/filesystem
touch ${PI_FILESYSTEM_ROOT}/local/final.sh
#cp -R ${POSTINSTALL_LOCAL}/* ${PI_FILESYSTEM_ROOT}/local/
chmod +x ${PI_FILESYSTEM_ROOT}/local/final.sh

rm -f ${POSTINSTALL_SCRIPT_ROOT}/postinstall.tar.gz

# When we compress the postinstall scripts, make sure the archive discards the path (it in decompressed in the right place), and that it excludes the .svn directory.
echo -n "Creating postinstall.tar.gz... "
tar cfz ${POSTINSTALL_SCRIPT_ROOT}/postinstall.tar.gz -C ${PI_FILESYSTEM_ROOT} .
echo "Done."

echo -n "Copying postinstall.tar.gz to /var/www/html/... "
cp ${POSTINSTALL_SCRIPT_ROOT}/postinstall.tar.gz /var/www/html
echo "Done."
