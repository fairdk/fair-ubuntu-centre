Cloning hard drives
===================

In order to obtain a data drive for the server, clone a **master**
(or **source**) hard drive onto a **target**. There is nothing special about
the master, just that it's a hard drive that you keep safe such that other
hard drives can be cloned from it.

.. tip::
    Keep your hard drives labeled with a version (or date). Confusion can be
    quite costly timewise.

.. warning::
    Never deploy your last master copy, it is recommendable to have 2 master
    copies.

.. tip::
    Before using the a disk copy in a school, consider setting up the server at
    your own location and testing it there.

As of 2018, the data footprint is roughly 550 GB.


Cloning to same capacity disk
-----------------------------

If - say - you have a ``source`` disk with a 1 TB capacity and you are cloning
to a ``target`` that is also a 1 TB drive, you should use a SATA docking
station. This is the much faster option.

In order to optimize the chances for correct copies, make sure to monitor the
copying process in case of electrical blackouts. You may also use a UPS to
protect against both blackouts and power surges. If you cannot get a UPS, a
power surge protector is also helpful, in cases where the SATA docking station
is affected by power surges.


Copying to different capacity disk
----------------------------------

A step-by-step guide is provided below, but firstly some background...

Cloning to a *larger* ``target``: If - say - you have a ``source`` disk with
a 1 TB capacity and you are cloning to a ``target`` that is 2 TB, you can clone
with a SATA docking station, but you will *not* be able to use the disk at its
2 TB capacity afterwards, it will report as a 1 TB file system (the size of
the ``source`` file system).

Cloning to a *smaller* ``target``: This is **not** possible with a SATA
docking station.

When you have different capacity ``source`` and ``target``, the best method is
to copy file-by-file using mounted filesystems. You do this by connecting both
drives with a USB dock. Use USB 3.0 if available, it is much faster (the USB
plug in your computer is usually colored blue for 3.0 ports). You can also
connect both drives to the motherboard using a SATA cable.

When both drives are connected, you may have to format the destination drive.
It should be labeled ``FAIR`` and the file system must be ``ext4``.

After both drives have been mounted, observe that ``source`` and ``target`` are
mounted as ``FAIR`` and ``FAIR1``, but which is which? You have to find out
manually. The file systems of both drives have identical labels ``FAIR``, but
the operating system makes sure to mount them in separate locations.

.. warning:: Before you copy, make sure that you know which is the source and
  which is the target. Be aware that they can swap if you unplug drives or
  reboot the computer.

Glossary
~~~~~~~~

* **Drive**: When we just say "drive", we mean the whole drive and not something
  specific.
* **Partition table**: A drive will always have one single partition table,
  which says where the partitions are located.
* **Partition** A section of a hard drive. If you use Windows, you can recall
  it has **drive letters** such as ``C:\``. This actually denotes a partition.
  On Unix and Linux, partitions can be found anywhere in a different tree
  structure.
* **Mounting**: A partition is *mounted* on to the root file system, meaning
  that for instance, you can have a path called ``/media/username/drive-label``
  and it's our way of saying that when you read or write files anywhere in
  that hierarchy.
* **Formatting**: The action of formatting something means to create a new file
  system on a partition.
* **File system**: A file system is a certain way of organizing files and
  folders on a partition. Different operating systems use different file
  systems. On Linux, the most normal system is called ``Ext4``.
* **Device node**: When a file system isn't mounted, it is often refered to by
  its *device node*, such as ``/dev/sda1``. This is a special path where you
  cannot put files or folders. But you can use it to refer to a partition or
  drive. The disk itself doesn't have a number and appears like ``/dev/sda``,
  and each partition is refered to by a number, for instance ``/dev/sda3``.

Step-by-step
~~~~~~~~~~~~

#. Start by plugging in the ``source`` drive. It will be available in the
   location ``/media/<username>/FAIR``. You can verify by running this from
   command line:

   .. code-block:: bash

       ls /media/<username>/FAIR  # Replace <username> with your username.

   This should display a list of files, such that you can verify that the
   ``source`` drive is indeed *mounted* here. If you want to see which drives
   are currently mounted, and where, run:

   .. code-block:: bash

       lsblk  # Lists all devices and partitions and where they're mounted
       mount # This lists everything mounted but is a bit harder to read

#. You need to format a new partition on the ``target`` drive. Use the **Disks**
   program that is installed by default in Ubuntu. The partition should be
   labeled ``FAIR`` and the file system must be ``Ext4``. If there is something
   already on the drive, the easiest option is to use the *Format Disk* option,
   which will generate a new *partition table*, on to which you can add a
   partition using the entire capacity of the drive.

#. After formatting the ``target`` partition, make sure that it is mounted.
   You can also use the **Disks** program to mount the partition. Use the
   ``lsblk`` command to see which drives and partitions are mounted.

#. When both ``source`` and ``target`` drives are mounted and ready, you must
   use the ``rsync`` command to copy files. The program makes it possible to
   resume in case you are interrupted. This is crucial, becase depending on the
   USB or SATA connection, the copying process can take as much as 12 hours,
   and you may experience power cuts.
   
   The command is as follows, assuming that ``source`` is mounted in
   ``/media/<username>/FAIR``!!

   .. code-block:: bash

      # This command replaces $USER with your username automatically.
      rsync -av --stats /media/$USER/FAIR /media/$USER/FAIR1

