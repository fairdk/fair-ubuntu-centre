#!/bin/bash

if [ -f /etc/computer_label_id ]
then
	label=`cat /etc/computer_label_id`
	# Don't care about errors otherwise we risk blocking lightdm
	result=`wget -q -O /dev/null http://intranet.fair/technicians/computer/logout/$label/$USER/ 2>&1`
fi

exit 0
