#!/bin/bash
echo "Reparing mysql can take a long time depending on which table has been corrupted."
echo "It can take up to 15 min."
read -p "Continue? [Y/n]" yn

if [ $yn == "n" ]
then
	echo "Exiting"
	exit
fi
stop mysql
myisamchk --verbose --force --fast --quick --update-state \
          --key_buffer_size=512M --myisam_sort_buffer_size=512M \
          --read_buffer_size=64M --write_buffer_size=64M \
          /var/lib/mysql/wikipedia/*.MYI
start mysql
