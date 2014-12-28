#!/bin/bash

# Put all customized settings here, example:
# export FAIR_ARCHIVE_PATH=/my/custom/path

export FAIR_ARCHIVE_PATH=/var/FAIR
export USE_FAIR_DISK=0
export FAIR_SERVER_HOSTNAME="development-fair-server"

# The PING_Clients script is not wanted under development
export FAIR_CONF_D_SKIP=( "ping_clients.sh" "01-repository.sh" )
