#!/bin/bash
if [ -n "${SCRIPT_ROOT}" ]; then

        echo "Globals already defined"
else
        SCRIPT="`readlink -e $0`"
        SCRIPTPATH="`dirname $SCRIPT`"
        echo "Including global variables"
        export SCRIPT_ROOT=$SCRIPTPATH/..
        . $SCRIPTPATH/../config/default_cfg.sh
fi

echo "---------------------------------------"
echo "Installing intranet                    "
echo "---------------------------------------"

apt-get install python-virtualenv libapache2-mod-wsgi