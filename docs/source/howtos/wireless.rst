Setting up a Wireless center
============================

.. warning:: It is not recommended to do Wireless centers, as the installation and booting from networks have been proven very difficult.


Prerequisits
____________

* A wireless access point (AP) with bridging enabled, i.e. not acting as a router
* Server connected to AP.
* Server configured with a local overlay for wireless setups.
* mini.iso prepared on a USB for booting clients before installing

  * Obtain mini.iso:
    `http://archive.ubuntu.com/ubuntu/dists/trusty/main/installer-i386/current/images/netboot/ <http://archive.ubuntu.com/ubuntu/dists/trusty/main/installer-i386/current/images/netboot/>`__

* Copy the .iso image to a USB flash, this will overwrite everything of the USB:

  * Insert flash, it may be automatically mounted so should be unmounted if it's mounted.

    * To see what is mount: ``mount``
    * To unmount: ``umount /dev/sdX1``
    * To copy: ``sudo dd bs=4M if=Downloads/mini.iso of=/dev/sdb``

  * Now the flash is bootable


Installing a client
-------------------

- Turn on the machine, press for instance F12 and choose to boot from USB
- Press TAB to edit the first "Install" option for Ubuntu
- Delete the ``quiet`` part.
- Put: ``ks=http://192.168.10.1/ks.cfg ksdevice=WLAN0``
- When installing, you should be able to choose the wireless network that you have configured


Configuring DIR-635 access points
---------------------------------


#. Reset the device
#. Attach to a machine and obtain DHCP from the AP
#. Connect to ``192.168.0.1``
#. Setup an un-encrypted wireless, DO NOT REBOOT YET
#. Go to Network

   #. Disable DHCP
   #. Disable DNS relay
   #. Give the router a static IP, i.e. ``192.168.10.2`` (must be unique to your network!)

#. Go to Advanced and disable features you know are useless.
#. Reboot device
#. Connect to server on one of the Switch ports, not the internet/WAN port


.. tip:: Use two access points and configure them on separate channels.

Booting from the network
------------------------

Once the server is installed, and the network is ready, you need to boot from the network.

However, as computers do not support TFTP via WIFI, you need to:

#. Boot from a USB flash
#. Tell the Ubuntu installation program (debinstall) where to find the configuration for automatic installations, and to configure the WIFI in order to retrieve this list.

Creating the bootable USB flash
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve the mini.iso for installing Ubuntu, one which is from the same date as the data drive, but never newer!

 * 14.04: http://archive.ubuntu.com/ubuntu/dists/trusty/main/installer-i386/current/images/netboot/

.. warning:: The USB flash you use will be overwritten!

Once downloaded to your Ubuntu/Linux computer:

Run the command ``df -h`` and notice which device name corresponds to your USB. If you get this wrong, you can overwrite your hard drive. The device name is ``/dev/sdX``, where X is some letter. ``/dev/sda`` is your hard drive.

Make sure that no programs are using or blocking the USB flash. Run the command ``mount`` to see what drives are in use. If you see your USB flash's device name, run the command ``umount /dev/sdX1`` to *unmount* it.

When you know the device name of the USB, run the following command::

    dd if=/path/to/iso of=/dev/sdX bs=4096


Booting the flash
~~~~~~~~~~~~~~~~~

As you are booting from the flash, you have to edit the default entry by adding the following lines::

    ks=http://192.168.10.1/ks.cfg ksdevice=wlan0 netcfg/wireless_essid=FAIR

.. tip:: Do not start too many machines, because the wireless network easily gets congested. 5-10 machines is often the limit.
