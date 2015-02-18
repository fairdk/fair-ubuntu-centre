fair-ubuntu-centre
==================

**This is the Trusty / Ubuntu 14.04 edition**

This project is an attempt to structure and open source the efforts of [FAIR](http://www.fairinternational.org) in Malawi.
The goal of the project is to distribute open source software and open access knowledge and media repositories to remote areas with no internet connectivity, rather than wasting efforts on expensive and/or badly-functioning mobile networks. More universally speaking, it could be said that the project attempts to do ICT4D but without any broadband internet connection in the actual deployments of the project.

The project provides the scripts necessary to configure a normal desktop installation of Ubuntu 14.04 to become a
network server, TFTP install server, and HTTP intranet server for a variety of offline resources (hereunder the full Ubuntu repositories!).

In order to use the scripts, a (possibly external) hard drive must be created with a number of optional resources.

Everything is tested and in use at 10 school centres. The next big step is to start structuring the codebase and writing documentation to enable usage even outside the scope of FAIR projects.

Requirements
------------

* Ubuntu 32 bit repositories: 64+ GByte

Obtaining data
--------------

FAIR has the data dumps of Ubuntu, Kiwix, KA Lite, and various other content providers of free movies and e-boots. They are not currently offered by
online sources, please get in touch with us for any data exchange.

TODO
----

See [TODO.md](TODO.md)

Documentation
-------------

As of today, there is still a pending documentation project and a guide for system maintainers in the works.

Philosophy
----------

Everything in here is implemented in flat-out BASH scripts. It's not as if we
didn't feel like using a different language, however to a new system administrator
wanting to know what's going on, the choice of a scripting language identical
to the command line is quite a lot easier.

Background
------------------

## Choice of Linux OS

The project is based on 14.04 LTS. The policy is to always use an LTS that has been out for at least 6 months.

### Discussion

However, we do ponder about providing backwards compatible setups. Experiences say that school
computers are better off with less machine intensive Linux desktops, and that
newer versions do not always provide better performance. For instance, we see that Ubuntu 10.04
is actually providing better responsiveness on older hardware (256 MB, <2 GHz CPU).

Another alternative would be to add installation configurations that gave the choice of Lubuntu
or Xubuntu desktops.
