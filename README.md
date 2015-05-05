fair-ubuntu-centre
==================

**This is the Trusty / Ubuntu 14.04 edition**

[![Docs](https://readthedocs.org/projects/fair-ubuntu-centre/badge/?version=latest)](http://fair-ubuntu-centre.readthedocs.org/)

This project captures the efforts of [FAIR](http://www.fairinternational.org) in Malawi. As the number
of ICT centres steadily grows, the project adds more efficiency and is improving its architecture to
accomodate development of new features and future management of individual centre setups.

Fundamentally, these scripts deliver a fully-automated self-configuration of a default Ubuntu desktop
to transform it into a server for the ICT centres, provided that it has access to a *data drive*
containing a copy of the Ubuntu repositories. The server provides a fully functional Ubuntu repository
combined with TFTP services for installing client desktops.

Offline resources
-----------------

In addition to LAN-managed installations of Ubuntu, the server can also provide a range of contemporary
offline projects, such as KA Lite and Kiwix, together with an Intranet-like service that collects the
various resources for internet browser access.

Deployments
-----------

The codebase is tested at a couple of centres and an upgrade from a 12.04-based deployment is
taking place (March '15) on 8 other centres.

Development efforts seek to take the project beyond FAIR's deployments and to modularize software features
and server's resources at an individual centre level.

Furthermore, we are adding functionalities and documentation to support the workflow of
technicians working in the field.

Requirements
------------

* Additional hard drive containing data, *Data Drive*, see Obtaining Data (TODO: Add drive layout specs)
   * Ubuntu 32 bit repositories: 120+ GByte (fixed requirement)
   * KA Lite (optional)
   * Kiwix (optional)
   * Various Ebooks and Documentary movies at unspecified locations
     as referenced by Intranet pages.
* Installscripts copied to a USB flash
* Server hardware: SATA host recommended.
* Server processor requirements: None really, storage is the main feature
* Server memory: 1+ GB, more memory is recommended as it allows faster response times from HTTP servers,
  WSGI applications, and Kiwix services accessing lots of disk data.


Obtaining Data
______________

FAIR has the data dumps of Ubuntu, Kiwix, KA Lite, and various other content providers of free movies and e-boots. They are not currently offered by
online sources, please get in touch with us for any data exchange.


Background
----------

The primary goal of the project is to distribute open source software and open access knowledge and media repositories
to remote areas with no internet connectivity, rather than wasting efforts on expensive mobile connectivity.
More universally speaking, it could be said that the project attempts to do ICT4D but without any broadband
internet connection in the actual deployments of the project.

Secondary or supplementary to the primary goal, we are seeking efficiency in terms of deploying new centres
and maintaining existing ones. Because of this, the deployment effort mainly has to do with setting up the
physical environment of the ICT centres and not the 

The project provides the scripts necessary to configure a normal desktop installation of Ubuntu 14.04 to become a
network server, TFTP install server, and HTTP intranet server for a variety of offline resources (hereunder the full Ubuntu repositories!).

In order to use the scripts, a (possibly external) hard drive must be created with a number of optional resources.

### Choice of Linux OS

The project is based on Ubuntu 14.04 LTS (with the edubuntu-desktop package installed by default).
A basic policy is to use Ubuntu's LTS (Long-Term-Support) after it has been out for at least 6 months.

#### Discussion

We do aim a lot at providing backwards compatible setups. Experiences say that school
computers are better off with less machine intensive Linux desktops, and that
newer versions do not always provide better performance. For instance, we see that Ubuntu 10.04
is actually providing better responsiveness on older hardware (256 MB, <2 GHz CPU).

As much as Ubuntu, the Linux kernel, X drivers etc. are adding support for new hardware,
older hardware is becoming less supported as the test audience shrinks.

Another alternative would be to add installation configurations that gave the choice of Lubuntu
or Xubuntu desktops.



TODO
----

See [TODO.md](TODO.md)


Philosophy
----------

Everything in here is implemented in flat-out BASH scripts. It's not as if we
didn't feel like using a different language, however to a new system administrator
wanting to know what's going on, the choice of a scripting language identical
to the command line will make the process of server installation and configuration
more transparent.

