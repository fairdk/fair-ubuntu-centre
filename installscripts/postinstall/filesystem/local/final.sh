#!/bin/bash

useradd -m -U -s /bin/bash manager
usermod manager --comment "Manager"
echo "manager:morebandwidth" | chpasswd
adduser manager sudo
adduser manager adm 
adduser manager dialout
adduser manager fax
adduser manager cdrom
adduser manager floppy
adduser manager tape
adduser manager dip
adduser manager video
adduser manager plugdev
adduser manager fuse
adduser manager lpadmin
adduser manager sambashare
adduser manager epoptes

cp -rf /home/teacher/.ssh /home/manager/
chmod 700 /home/manager/.ssh

useradd -m -U -s /bin/bash online
usermod online --comment "Online user"
adduser online fax
adduser online cdrom
adduser online floppy
adduser online tape
adduser online dip
adduser online video
adduser online plugdev
adduser online fuse
adduser online lpadmin
adduser online sambashare

# Render passwords useless
# (passwd -d is not an option because that makes lightdm
#  opt for password-less login)
echo "student:dkfhksjfhk234jda" | chpasswd
echo "teacher:dkfasdasdg3hksjfhk234jda" | chpasswd
echo "online:dasdk2fhksjf234hk234jda" | chpasswd

chmod +x /home/manager/Desktop/Manage\ Clients.desktop
chown -R manager.manager /home/manager/

chmod 700 /home/manager/.ssh

chmod +x /etc/network/whoami.sh
chmod +x /etc/lightdm/*sh

# Remove student user from the group that has passwordless login
gpasswd -d student nopasswdlogin

