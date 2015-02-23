#!/bin/bash

# Here we set up the NFS server, and the directories that it depends on.
# We also create the teacher account here.

echo "---------------------------------------"
echo "Installing NFS server                  "
echo "---------------------------------------"

echo "Blacklisting IPv6 modules due to a bug"

sed -i 's/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"/GRUB_CMDLINE_LINUX_DEFAULT="quiet splash ipv6.disable=1"/g' /etc/default/grub

if [ -f /proc/sys/net/ipv6/conf/all/disable_ipv6 ]
then
	echo "Switching off IPv6"
	echo 1 > /proc/sys/net/ipv6/conf/all/disable_ipv6
fi

# Ensure there's a teacher account
if [ ! -d /home/teacher ]
then
	echo "Creating a teacher account and a shared NFS folder"
	useradd -m -U -s /bin/bash teacher
	echo "teacher:${TEACHER_PASSWORD}" | chpasswd
fi

# Ensure it has a materials folder
if [ ! -d /home/teacher/materials ]
then
	mkdir -p /home/teacher/materials
	echo "Put documents here, and students will be able to access them from their Desktop" > /home/teacher/materials/README.txt
	chown teacher.teacher /home/teacher/materials
fi

# The server should be installed BEFORE modifying /etc/exports, otherwise a prompt appears with no automatic way to circumvent it...
apt-get install -y -q nfs-kernel-server

# Define which folders to share
echo "${FAIR_DRIVE_MOUNTPOINT}/ubuntu/ *(ro,no_subtree_check,no_root_squash)" > /etc/exports
echo "${FAIR_DRIVE_MOUNTPOINT}/data/movies/ *(ro,no_subtree_check,no_root_squash)" >> /etc/exports
echo "/home/teacher/materials/ *(rw,no_subtree_check,no_root_squash)" >> /etc/exports

/etc/init.d/nfs-kernel-server restart

# Ensure that the export is created
exportfs -a
