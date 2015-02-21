#!/bin/bash
rm /usr/share/X11/xorg.conf.d/force_vesa.conf
rm /etc/grub.d/40-force_vesa
echo "Removed force_vesa.conf"
