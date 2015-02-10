#!/bin/bash

BRANCH=${1:-"master"}

if [ "$1" = "clean" ]
then
	if [ -d build ]
	then
	    rm -rf build
	fi
fi

mkdir -p build

git archive $BRANCH installscripts/ | tar x -C build/

cd build/installscripts/data/intranet/
if [ ! -d virtualenv ]
then
	echo "Getting wagtail build dependencies"
	sudo apt-get install python-dev python-pip g++ libjpeg62-dev zlib1g-dev
	virtualenv virtualenv
	virtualenv --relocatable virtualenv
fi

echo "Installing requirements.txt..."
source virtualenv/bin/activate
pip install -r fairintranet/requirements.txt
cd fairintranet
python manage.py collectstatic
cd ../

cd ../../../

echo "Creating tarball..."
tar cfz installscripts.tar.gz installscripts
