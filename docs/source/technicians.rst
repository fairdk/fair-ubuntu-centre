Setting up a server
===================

Server requirements
-------------------

The following items are necessary for setting up a server:

* Data drive (1-2TB) preloaded with all of the data
* A server, should be a machine with a decent memory, CPU, and stable fans
* A USB flash containing default Ubuntu Desktop (14.04 32-bit)
* A USB flash containing the FAIR `installscripts <http://github.com/fairdk/fair-ubuntu-centre>`__
* If previously installed, copy the old configuration of the centre to installscripts/config/local/name-of-site

Installation procedure
----------------------

#. Install Ubuntu 14.04 32-bit on the server, choose to erase everything if there is already something there. Call the user and the password something that was agreed that other technicians can know (not the school).
#. Shutdown the server after installation
#. Insert the data hard drive on secondary SATA port
#. Boot the system and log in
#. Insert USB with installation scripts
#. Make sure that the hard drive is mounted, you can use command "mount" or click the hard drive's icon in the application bar, bottom left
#. Now open a terminal, CTRL+ALT+T
#. Type ``sudo bash`` to get a command line with administration privileges
#. Go where the USB flash is mounted: ``cd /path/to/usb-flash``, for instance "/media/fair/installscripts".
#. Go to the "installscripts" folder, for instance, ``cd fair-ubuntu-centre``. This folder should contain "install.sh", the main program that transforms the newly installed Ubuntu desktop to an ICT centre server.
#. Remember that you can always type ``ls`` to see the contents of a folder.
#. Run ``./install.sh`` and the installation begins. There might be questions during the end of the installation, but the first part will take some minutes, so you can go for tea.
#. At the end, the installation asks for a "Local overlay", that means that specific configurations for this centre is added. It will ask about each folder that it finds in "installationscripts/config/local". This should include the centre, that you are working on.


Creating a new local overlay
----------------------------

#. Go to the installscripts/config/local folder::

      bash
      cd installscripts/config/local

#. Look at what's there and select a previous centre where the setup is most similar to the one you are doing and copy that one::

      cp -R other-centre new-centre

#. Re-run the last part of the install.sh job::

      cd ../../
      ./install.sh 98-local.sh


Changing the local configuration
________________________________


If you need to change files in the local configurations, you should read the documentation for creating local configurations. But the overall idea is this:

#. Make changes to the files
#. Re-run the last part of the install.sh job::

       cd ../../
       ./install.sh 98-local.sh


Re-running the local configuration on all machines
__________________________________________________


If you have already installed all machines and have made ammendments (e.g. added a new standard program, user or printer driver), you can re-run the post-installion by running this command on the server::

    cd /media/fair/usb-flash/path/to/installscripts/
    python scripts/deploy/rerun_postinstall.py

.. warning:: Only machines that are switched on and correctly attached to the network will be affected.


Machines that cannot boot from network
______________________________________

Create a CD / USB flash with gPXE. You can obtain the .iso file from:

`http://rom-o-matic.net/gpxe/gpxe-#.0.1/contrib/rom-o-matic/ <http://rom-o-matic.net/gpxe/gpxe-#.0.1/contrib/rom-o-matic/>`__

* Copy the .iso image to a USB flash, this will overwrite everything of the USB:
* Insert flash, it may be automatically mounted so should be unmounted if it's mounted.

  * To see what is mount: ``mount``
  * To unmount: ``umount /dev/sdX1``
  * To copy: ``sudo dd bs=4M if=Downloads/gpxe.iso of=/dev/sdX``

* Now the flash is bootable

Otherwise, burn the iso to a CDR, but remember that you should burn an *image* not a file.


After installing
----------------

Make sure that you have copied the contents of the installscripts to "/root/" so another technician can know what was used for the installation::

    cd /media/fair/usb-flash/path/to/installscripts/
    cp -R . /root/

Make sure to also copy the configuration overlay, for instance::

    cd /media/fair/usb-flash/path/to/installscripts/config/local
    cp -R . /root/

    
Installing clients (student computers)
--------------------------------------

Make sure that network booting is enabled in the BIOS. When booting from the
network, select the ``Automatic Ubuntu install`` option which will install
everything without asking questions.

After the installation is completed, the client will reboot
**but it's not yet finished!**

It will complete a *post-install* procedure, which is a custom script
that will run, also installing additional software.

This process takes time, and even if you do not see any progress on the screen
for up to 20 minutes, just let the script finish.


Verifying an installed client
-----------------------------

It's important to check that the client has installed everything correctly,
because an interruption during the unattended intallation will sometimes cause
computers to be in a bad state.

Verify for instance:

* When logging in as a student, you receive the Gnome Classic desktop
  interface, which has the Applications + Places menu in the top left corner.
  Not the Unity desktop! If you are directed to the Unity desktop, log back
  out and select Gnome Fallback (Metacity) instead from the menu next to the
  username selection.

* That the ``student`` and ``teacher`` account are setup correctly, and that there
  is not password required for the ``student`` account.

* KA Lite videos are playing correctly.

* That the folder with *Materials For Students* is working and teachers can
  write to it.
