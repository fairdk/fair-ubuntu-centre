fair-ubuntu-centre
==================

This project is an attempt to structure and open source the efforts of [FAIR](http://www.fairinternational.org) in Malawi.
The goal of the project is to distribute open source software and open access knowledge and media repositories to remote areas with no internet connectivity, rather than wasting efforts on expensive and/or badly-functioning mobile networks. More universally speaking, it could be said that the project attempts to do ICT4D but without any broadband internet connection in the actual deployments of the project.

The project provides the scripts necessary to configure a normal desktop installation of Ubuntu 12.04 to become a
network server, TFTP install server, and HTTP intranet server for a variety of offline resources (hereunder the full Ubuntu repositories!).

In order to use the scripts, a (possibly external) hard drive must be created with a number of optional resources.

Everything is tested and in use at 10 school centres. The next big step is to start structuring the codebase and writing documentation to enable usage even outside the scope of FAIR projects.

TODO
----

See [TODO.md](TODO.md)

Documentation
-------------

As of today, there is still a pending documentation project and a guide for system maintainers in the works.

Background
------------------

### Choice of Linux OS

The project will continue to be based on Ubuntu 12.04 until the release of 14.04 has been out for at least 6 months.
Current experiences hint that school computers are better off with less machine intensive Linux desktop, hence Ubuntu 10.04
is actually providing a better user experience regarding the responsiveness of older hardware (256 MB, <2 GHz CPU).
