#!/bin/bash


# This file contains variables that can be customized for your installation.

export USE_USB_DISK=1

if [ ! -n "${SCRIPT_ROOT}" ]
then
	SCRIPT="`readlink -e $0`"
	SCRIPTPATH="`dirname $SCRIPT`"
	export SCRIPT_ROOT=$SCRIPTPATH
fi

# Where data from the FAIR project is located, should be a path that's available
# after installing, but if it's a removable drive, the installer will add it
# to /etc/fstab
# NO TRAILING SLASH
export FAIR_ARCHIVE_PATH=/media/FAIR

# Where data from the FAIR project is located, should be a path that's available
# after installing, but if it's a removable drive, the installer will add it
# to /etc/fstab
export FAIR_INSTALL_DATA=${SCRIPT_ROOT}/data/

export FAIR_SERVER_HOSTNAME="fair-server"

# Terminate each entry with a ;
export FAIR_CONF_D_SKIP=("ping_clients.sh")

# TO customize the distribution installed on the client, add files here...
export POSTINSTALL_LOCAL=${SCRIPT_ROOT}/config/custom_postinstall/

# Where all local overlays reside
export CONFIG_LOCAL=${SCRIPT_ROOT}/config/local/

# The conf.d directory
export FAIR_INSTALL_CONF_D=${SCRIPT_ROOT}/conf.d/

# Password for the teacher account, which is by default installed on all
# clients and has sudo access.
export TEACHER_PASSWORD=ilovestudents

# Turns off debconf prompts
export DEBIAN_FRONTEND=noninteractive

# Not so important
export FAIR_MYSQL_PASSWORD="fair"

# What's this!?
export INSTALL_OPTIONAL_SW=0
# The PING_Clients script is not wanted under development

# After the network is reconfigured, the network manager needs time to reconncet to the internet.  If you don't wait, and want to install new programs from the internet (instead of a local repository) it will fail.
export WAIT_FOR_NETWORK_RESET=20

# Put the IP address of your internet sevice provider's nameserver here.
# PJD: NOT USED YET!!
# export ISP_NAMESERVER_IP=89.150.129.22

# Overwrite everything with a local config
if [ -f "${SCRIPT_ROOT}/config/custom_cfg.sh" ]
then
	. ${SCRIPT_ROOT}/config/custom_cfg.sh
fi
