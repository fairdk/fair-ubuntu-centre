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


