Troubleshooting Q&A
===================

File system errors on boot
--------------------------

If either the server or student computers are complaining during boot:

* If the BIOS battery is dead, the clock of the computer will reset on reboot.
  This causes the filesystem to produce errors because timestamps of files are
  in the future. Resolution: Replace the BIOS battery on the motherboard.

* Electrical blackouts may cause unclean shutdowns of file systems. Select the
  option to fix the hard drive.

If you want information about a file system error, go to maintenance mode and
run this command::

    # Check all filesystems from /etc/fstab in verbose mode
    sudo fsck -A -V


Network problems
----------------

Symptom: Clients are not able to connect or boot because of network issues.
This typically means that while booting, the computer hangs for several minutes
with the Ubuntu logo.

If the server is up, and you know that it is accessible directly from its
screen and keyboard, then problems are likely caused by network cables or
switches. If all computers are unable to connect, try these options:

* Make sure network cables are properly plugged in.
* Check that the switches are on.
* Use a LAN tester to check cables, especially the one from the server.
* Check that cables are not causing loopbacks, for instance if a network cable
  is connected to a switch at both ends.


Blackouts
---------

While installing the server
___________________________

The installation can be safely resumed and will pick up from where it left.
Just boot the default Ubuntu and re-locate and start ``install.sh``, following
the normal instructions.


While installing a client
_________________________


If the installation is disturbed in the first phase, installing the base system
(before rebooting the client), then you need to restart "Automatic Ubuntu
install".

If the installation is disturbed after the first reboot, you can do this to
save time::

    # Press CTRL+ALT+F1
    # Log in as teacher
    # In the command line after logging in, type...
    $ sudo bash
    # cd /root
    # bash rerun-postinstall.sh
