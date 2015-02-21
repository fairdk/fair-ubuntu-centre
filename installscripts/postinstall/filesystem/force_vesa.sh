#!/bin/bash

echo 'Section "Device"' > /usr/share/X11/xorg.conf.d/force_vesa
echo '  Identifier "Configured Video Device"' >> /usr/share/X11/xorg.conf.d/force_vesa
echo '  Driver "vesa"' >> /usr/share/X11/xorg.conf.d/force_vesa
echo 'EndSection' >> /usr/share/X11/xorg.conf.d/force_vesa
