Background
==========

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

Currently
---------

The 14.04 32bit setup is still deployed and maintained in Malawi as of April 2018.

Development efforts seek to take the project beyond FAIR's deployments and to modularize software features
and server's resources at an individual centre level.

We are adding functionalities and documentation to support the workflow of technicians working in the field.

Roadmap
-------

The next upgrade will contain 18.04 for 64 bit, furthermore:

* Replacing KA Lite with `Kolibri <http://learningequality.org/kolibri>`__
* Improving modular structures
* Separating installation and configuration steps: Supporting a workflow whereby servers are installed before arriving to their target destination.

Choice of Linux OS
------------------

The project is based on Ubuntu 14.04 LTS (with the edubuntu-desktop package installed by default).
A basic policy is to use Ubuntu's LTS (Long-Term-Support) after it has been out for at least 6 months.


Discussion
----------

We do aim a lot at providing backwards compatible setups. Experiences say that school
computers are better off with less machine intensive Linux desktops, and that
newer versions do not always provide better performance. For instance, we see that Ubuntu 10.04
is actually providing better responsiveness on older hardware (256 MB, <2 GHz CPU).

As much as Ubuntu, the Linux kernel, X drivers etc. are adding support for new hardware,
older hardware is becoming less supported as the test audience shrinks.

Another alternative would be to add installation configurations that gave the choice of Lubuntu
or Xubuntu desktops.


Philosophy
----------

Everything in here is implemented in flat-out BASH scripts. It's not as if we
didn't feel like using a different language, however to a new system administrator
wanting to know what's going on, the choice of a scripting language identical
to the command line will make the process of server installation and configuration
more transparent.

