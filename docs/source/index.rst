An Offline Digital Library
==========================

This project automatically configures a server for a Digital Library.
Client computers for students/users are then installed through PXE netboot.
The server contains a number of offline educational resources, together with
the full Ubuntu software repositories.

This documentation is intended for technicians working in the field to deploy
and maintain such Digital Libraries. 

**This is the Ubuntu 14.04 edition**

Contents
--------

.. toctree::
   :maxdepth: 2
   
   technicians
   checklist
   howtos/index
   troubleshooting
   background


This project captures the efforts of `FAIR`_ in Malawi. As the number
of ICT centres steadily grows, the project adds more efficiency and is improving its architecture to
accomodate development of new features and future management of individual centre setups.

Fundamentally, these scripts deliver a fully-automated self-configuration of a default Ubuntu desktop
to transform it into a server for the ICT centres, provided that it has access to a *data drive*
containing a copy of the Ubuntu repositories. The server provides a fully functional Ubuntu repository
combined with TFTP services for installing client desktops.

.. _FAIR: http://www.fairinternational.org


Offline resources
-----------------

In addition to LAN-managed installations of Ubuntu, the server can also provide a range of contemporary
offline projects, such as KA Lite and Kiwix, together with an Intranet-like service that collects the
various resources for internet browser access.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

