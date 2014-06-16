echo "---------------------------------------"
echo "X11vnc for connecting graphically to server"
echo "---------------------------------------"


apt-get install -y -q x11vnc
cp ${FAIR_INSTALL_DATA}/etc.init.d.x11vnc /etc/init.d/x11vnc
chmod +x /etc/init.d/x11vnc
update-rc.d x11vnc start 99 4 5 .

