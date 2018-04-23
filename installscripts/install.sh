#!/bin/bash

# PJD: Important design consideration:  This script should be able to upgrade an existing server,
# therefore all operations must start by removing and old crap and ensuring a complete
# overwrite of the contents.  This feature can be especially handy when developing too :).
# Could consider starting script with a warning WILL ERASE EXISTING INSTALLATION, ARE YOU SURE...

# Enable tracebacks
# Save my own path
INSTALL_SH_DIR=`pwd .`

# Check dependancies- permissions, and access to media drive
if !(whoami | grep "root" -q)
then
	echo "Only root can run this!"
	echo ""
	echo "Run the program as root, ie.:"
	echo "sudo bash install.sh"
	exit 1
fi

set -eu

bash $INSTALL_SH_DIR/traceback.sh

# Include variables defined externally
. ./config/default_cfg.sh

echo ""
echo "This script will upgrade an Ubuntu installation to become a server"
echo ""
echo "You can abort the script at any time with CTRL+C but this will"
echo "not undo any changes made to the system."
echo ""
echo "You can re-run the script and it will automatically resume any"
echo "remaining operations"
echo ""

read -p "Press ENTER to continue or CTRL+C to abort..."
echo ""

echo "---------------------------------------"
echo "Starting FAIR install"
echo "---------------------------------------"

# Stop the script that turns off the server in case it's installed
if [ -f /etc/init.d/ping_clients ]
then
	set +o errexit
	echo "Stopping ping_clients (so server does not automatically switch off)"
	/etc/init.d/ping_clients stop
	set -o errexit
fi

if [ ! -d $FAIR_ARCHIVE_PATH ]
then
	echo "FAIR USB drive not detected in $FAIR_ARCHIVE_PATH"
	exit 1
fi

echo "---------------------------------------"
echo "Installing config files"
echo "---------------------------------------"

# If the script was called with a command line parameter, the parameter must be the name of a script in Conf.d.  Only that script is excuted
command_arg1=${1:-""}
if [ ! "$command_arg1" = "" ]
then
	echo "Running $1"
	. "$FAIR_INSTALL_CONF_D/$1"
else
	# If no parameters were used when calling this script, all files in conf.d are executed.
	for file in `ls "$FAIR_INSTALL_CONF_D"`
	do
		if [ -f "$FAIR_INSTALL_CONF_D/$file" ]; then
			skip="no"

			# Check the list of files to skip...
			for fskip in "${FAIR_CONF_D_SKIP[@]}"
			do
				if [ "$fskip" == "$file" ]; then
					skip="yes"
				fi
			done

			if [ $skip = "no" ] ; then
				. $FAIR_INSTALL_CONF_D/$file
				cd $INSTALL_SH_DIR
			else
				echo "Skipping $file"
			fi
		fi
	done
fi


echo "---------------------------------------"
echo "Creating client postinstall package    "
echo "---------------------------------------"
cd $INSTALL_SH_DIR
bash postinstall/make_postinstall.sh


echo ""
echo ""
echo "All the installscripts have finished without errors!"
echo ""
echo "You may now start using the server :)"
