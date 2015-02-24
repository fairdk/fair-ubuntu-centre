#!/bin/bash
label=`cat /etc/computer_label_id`
wget -q -O /dev/null http://intranet.fair/technicians/computer/logout/$login/$USER 2>&1
