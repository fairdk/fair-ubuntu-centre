#!/bin/sh

# Tested on 14.04
xdg-settings set default-web-browser firefox.desktop

# Reset the theme
gsettings reset-recursively org.gnome.desktop.interface

