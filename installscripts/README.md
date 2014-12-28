# How to install the server

## Preparing the server OS

Install a normal Ubuntu 14.04 Desktop or Server edition depending on your own preference.

The choice of user can be customized, however if it's a FAIR project, call the user "fair".

## Making data accessible

All of the data should reside on a partition mounted in `/media/FAIR` or `/media/fair/FAIR`

The easiest way to make this happen, is by adding a label on a partition and 
calling it `FAIR`. That way, the mount point will be predictable and
automatically detected.

Data can be on a USB disk, however this setup is not recommended for the
following reasons:
  
  * USB drives are more volunerable, casings are often cheap and overheat.
    Furthermore, modern USB drives have been known to put unpredictable
    hardware, so for instance if you buy a Samsung, you get some cheap Seagate
    drive inside the casing.
  * USB interface is slower than SATA.
  * It is easy to remove so it will get removed.

Best of all: If you want a quality hard drive, it's cheaper to buy as an
internal drive.

One rule is important, though: ALWAYS keep your data on a separate drive. This
ensures future updates to be possible by swapping the drive and if it breaks
you can also swap it without a complete reinstallation.

## Running the install scripts

Put all of `installscripts` folder on a USB flash and run ./install.sh

(further instructions pending)

# About this folder

Please do not change files, because it breaks future updates! Put all local
customization in:

 - `config/custom_cfg.sh` - Global settings, executed before `install.sh` runs.
 - `config/local/my_site/` - Possibility to add custom filesystem overlays for
   both server and clients.

## The main installation

The main script `install.sh` is the one to execute. Global default configurations
are kept in `default_config.sh` and if it exists, then `custom_config.sh` will
be loaded after.

## Clients

The server is the main authority of how clients should be configured. Thus,
the whole configuration of a client is kept in the `client/` directory
that has its own structure similar to the server's.

The client's scripts and data will be downloaded in the finalized state of
the client when booting for the first time.

### Order of execution in install.sh

1. `config/default_cfg.sh` is loaded to setup the default environment.
1. The install script looks for data sources
1. Network configuration is done
1. The Ubuntu source is loaded, presumably from a local data source
1. Base system is installed
1. Everything in `conf.d` is executed according to alphanumeric order.
1. The `dist` overlay is put in place. *This is done after conf.d such that everything installed during this process can be overwritten with new files.*
1. `config/local.sh` is executed, **this is where all individual configurations** should be kept, i.e. in directories in `config/local/`.

## config/

## conf.d/

Everything in this folder is executed and individual packages and their
configurations are installed using scripts in this folder.

## data/

This folder contains various files used by the scripts in `conf.d`. Scripts
should put their data files in a subdirectory.

## dist/

This is where files to be overlayed on the host server should reside.

