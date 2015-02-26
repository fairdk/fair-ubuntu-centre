Prerequisites
=============

 * 2TB Data drive preloaded with all of the data (make sure to note that there is a number on the hard drive)
 * A server, should be a machine with a decent memory, CPU, and stable fans
 * A USB flash containing default Ubuntu Desktop (14.04 32-bit)
 * A USB flash containing the FAIR installscripts (can be obtained from http://github.com/fairdk/fair-ubuntu-centre)
 * If previously installed, copy the old configuration of the centre to installscripts/config/local/name-of-site


Installation procedure
======================

1. Install a Ubuntu on the server, choose to erase everything if there is already something there. Call the user 'fair' and the password something that was agreed that other technicians can know (not the school).

1. Shutdown computer af installation

1. Insert the data hard drive on secondary SATA port

1. Boot the system and log in

1. Insert USB with installation scripts

1. Make sure that the hard drive is mounted, you can use command "mount" or click the hard drive's icon in the application bar, bottom left

1. Now open a terminal, CTRL+ALT+T

1. Type `sudo bash` to get a command line with administration privileges

1. Go where the USB flash is mounted: `cd /path/to/usb-flash`, for instance "/media/fair/installscripts".

1. Go to the "installscripts" folder, for instance, `cd fair-ubuntu-centre`. This folder should contain "install.sh", the main program that transforms the newly installed Ubuntu desktop to an ICT centre server.

1. Remember that you can always type `ls` to see the contents of a folder.

1. Run `./install.sh` and the installation begins. There might be questions during the end of the installation, but the first part will take some minutes, so you can go for tea.

1. At the end, the installation asks for a "Local overlay", that means that specific configurations for this centre is added. It will ask about each folder that it finds in "installationscripts/config/local". This should include the centre, that you are working on.


Common tasks
------------


Creating a new local overlay
_____________________________


1. Go to the installscripts/config/local folder:
       cd installscripts/config/local`
1. Look at what's there and select a previous centre where the setup is most similar to the one you are doing and copy that one.
       cp -R other-centre new-centre`
1. Re-run the last part of the install.sh job:
       cd ../../
       ./install.sh 98-local.sh

Changing the local configuration
________________________________


If you need to change files in the local configurations, you should read the documentation for creating local configurations. But the overall idea is this:

1. Make changes to the files
1. Re-run the last part of the install.sh job:
       cd ../../
       ./install.sh 98-local.sh


Re-running the local configuration on all machines
__________________________________________________


If you have already installed all machines and have made ammendments (e.g. added a new standard program, user or printer driver), you can re-run the post-installion by running this command on the server:

    cd /media/fair/usb-flash/path/to/installscripts/
    python scripts/deploy/rerun_postinstall.py


**NB!!** Only machines that are switched on and correctly attached to the network will be affected.


Machines that cannot boot from network
______________________________________

Create a CD / USB flash with gPXE. You can obtain the .iso file from:

http://rom-o-matic.net/gpxe/gpxe-1.0.1/contrib/rom-o-matic/

 - Copy the .iso image to a USB flash, this will overwrite everything of the USB:
   - Insert flash, it may be automatically mounted so should be unmounted if it's mounted.
     - To see what is mount: `mount`
     - To unmount: `umount /dev/sdX1`
     - To copy: `sudo dd bs=4M if=Downloads/gpxe.iso of=/dev/sdX`
 - Now the flash us bootable

Otherwise, burn the iso to a CDR, but remember that you should burn an *image* not a file.


After installing
================

Make sure that you have copied the contents of the installscripts to "/root/" so another technician can know what was used for the installation:

    cd /media/fair/usb-flash/path/to/installscripts/
    cp -R . /root/

Make sure to also copy the configuration overlay, for instance:

    cd /media/fair/usb-flash/path/to/installscripts/config/local
    cp -R . /root/


Setting up a Wireless center
============================

Prerequisits
------------

 - A wireless access point (AP) with bridging enabled, i.e. not acting as a router
 - Server connected to AP.
 - Server configured with a local overlay for wireless setups.
 - mini.iso prepared on a USB for booting clients before installing
   - Obtain from mini.iso:
     http://archive.ubuntu.com/ubuntu/dists/trusty/main/installer-i386/current/images/netboot/
 - Copy the .iso image to a USB flash, this will overwrite everything of the USB:
   - Insert flash, it may be automatically mounted so should be unmounted if it's mounted.
     - To see what is mount: `mount`
     - To unmount: `umount /dev/sdX1`
     - To copy: `sudo dd bs=4M if=Downloads/mini.iso of=/dev/sdb`
   - Now the flash is bootable

Installing a client
-------------------

 - Turn on the machine, press for instance F12 and choose to boot from USB
 - Press TAB to edit the first "Install" option for Ubuntu
 - Delete the "quiet" part.
 - Put: "ks=http://192.168.10.1/ks.cfg ksdevice=WLAN0"
 - When installing, you should be able to choose the wireless network that you have configured

Configuring DIR-635 access points:
----------------------------------

 1. Reset the device
 1. Attach to a machine and obtain DHCP from the AP
 1. Connect to 192.168.0.1
 1. Setup an un-encrypted wireless, DO NOT REBOOT YET
 1. Go to Network
    1. Disable DHCP
    2. Disable DNS relay
    3. Give the router a static IP, i.e. 192.168.10.2 (must be unique to your network!)
 1. Go to Advanced and disable features you know are useless.
 1. Reboot device
 1. Connect to server on one of the Switch ports, not the internet/WAN port

Tips
----

Tip: Do not start too many machines, because the wireless network easily gets congested. 5-10 machines is often the limit.

Tip: Use to access points and configure them on separate channels.
