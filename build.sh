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
if [ ! -d virtualenv ]
then
	echo "Getting wagtail build dependencies"
	sudo apt-get install python-dev python-pip g++ libjpeg62-dev zlib1g-dev python-virtualenv
	virtualenv virtualenv
	virtualenv --relocatable virtualenv
fi

echo "Installing requirements.txt..."
set +o nounset
source virtualenv/bin/activate
set -o nounset
pip install -r fairintranet/requirements.txt
cd fairintranet
python manage.py collectstatic --noinput
cd ../

cd ../../../

echo "Creating tarball..."
tar cfz installscripts.tar.gz installscripts
