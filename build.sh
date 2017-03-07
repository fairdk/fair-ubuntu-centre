#!/bin/bash

# Enable tracebacks
# Save my own path
SCRIPT="`readlink -e $0`"
SCRIPTPATH="`dirname $SCRIPT`"

set -eu
bash "$SCRIPTPATH/installscripts/traceback.sh"

BRANCH=${1:-$(git symbolic-ref HEAD | sed 's/refs\/heads\///')}

echo "Building on current branch '$BRANCH'..."
echo ""

if ! [ -d build ]
then
	mkdir -p build
fi

git archive $BRANCH installscripts/ | tar x -C build/

cd build/installscripts/data/intranet/

# Build virtualenv - only works on 32bit
if [ ! -d virtualenv ]
then
	echo "Getting wagtail build dependencies"
	sudo apt-get install python-dev python-pip g++ libjpeg62-dev zlib1g-dev python-pil
	# We need the version from pip!
	sudo pip install virtualenv==15.1.0
	virtualenv virtualenv

	echo "Installing requirements.txt..."
	set +o nounset
	source virtualenv/bin/activate
	set -o nounset
	# This is where things can break: We may be building on 64 bit but destined for 32 bit!
	pip install -r fairintranet/requirements.txt --no-use-wheel
	cd fairintranet
	python manage.py collectstatic --noinput
	cd ../
	deactivate
	virtualenv --relocatable virtualenv
fi

cd ../../../

echo "Creating tarball..."
tar cfz installscripts.tar.gz installscripts
