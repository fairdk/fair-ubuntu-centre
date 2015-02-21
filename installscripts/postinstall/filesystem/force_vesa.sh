#!/bin/bash

echo 'Section "Device"' > /usr/share/X11/xorg.conf.d/force_vesa.conf
echo '  Identifier "Configured Video Device"' >> /usr/share/X11/xorg.conf.d/force_vesa.conf
echo '  Driver "vesa"' >> /usr/share/X11/xorg.conf.d/force_vesa.conf
echo 'EndSection' >> /usr/share/X11/xorg.conf.d/force_vesa.conf

cp force_vesa.grub /etc/grub.d/40-force_vesa
