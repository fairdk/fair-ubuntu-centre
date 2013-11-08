#!/bin/sh
rm -Rf /root/postinstall
mkdir -p /root/postinstall
cd /root/postinstall
wget -O postinstall.tar.gz http://192.168.10.1/postinstall.tar.gz
tar xfz postinstall.tar.gz
./postinstall.sh
