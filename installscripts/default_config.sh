#!/bin/bash


# This file contains variables that can be customized for your installation.

export USE_USB_DISK=1

if [ ! -n "${SCRIPT_ROOT}" ]
then
	SCRIPT="`readlink -e $0`"
	SCRIPTPATH="`dirname $SCRIPT`"
	export SCRIPT_ROOT=$SCRIPTPATH
fi

# TO customize the distribution installed on the client, add files here...
export POSTINSTALL_LOCAL=${SCRIPT_ROOT}/config/custom_postinstall/

export CONFIG_LOCAL=${SCRIPT_ROOT}/config/local/

export FAIR_ARCHIVE_PATH=/media/FAIR

export TEACHER_PASSWORD=ilovestudents

export INSTALL_OPTIONAL_SW=0
# The PING_Clients script is not wanted under development

# After the network is reconfigured, the network manager needs time to reconncet to the internet.  If you don't wait, and want to install new programs from the internet (instead of a local repository) it will fail.
export WAIT_FOR_NETWORK_RESET=20

# Put the IP address of your internet sevice provider's nameserver here.
# PJD: NOT USED YET!!
# export ISP_NAMESERVER_IP=89.150.129.22
