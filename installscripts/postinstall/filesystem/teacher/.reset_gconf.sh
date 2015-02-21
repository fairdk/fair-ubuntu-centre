#!/bin/sh

# Tested on 14.04
xdg-settings set default-web-browser firefox.desktop

# Background
gconftool --recursive-unset /desktop
#gconftool -t string --set /desktop/gnome/background/picture_filename "file:///usr/share/backgrounds/edubuntu_default.png"
#gconftool -t string --set /desktop/gnome/background/picture_filename null
#gconftool -t bool --set /desktop/gnome/background/draw_background 1
#gconftool -t string --set /desktop/gnome/background/primary_color black

# Theme
gconftool -t string --set /desktop/gnome/interface/gtk_theme Ambiance
gconftool -t string --set /desktop/gnome/interface/icon_theme ubuntu-mono-dark
gconftool -t string --set /apps/metacity/general/theme Ambiance

gconftool -t bool --set /desktop/gnome/sound/event_sounds 0
gconftool -t bool --set /apps/bluetooth-manager/show_icon 0

