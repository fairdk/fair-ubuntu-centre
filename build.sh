#!/bin/bash

BRANCH=${1:-"master"}

if [ -d build ]
then
    rm -rf buid
fi

mkdir build

git archive $BRANCH installscripts/ | tar x -C build/

cd build/installscripts/data/intranet/
virtualenv virtualenv
virtualenv --relocatable virtualenv
source virtualenv/bin/activate
pip install -r fairintranet/requirements.txt

cd ../../../
tar xvfz installscripts.tar.gz installscripts