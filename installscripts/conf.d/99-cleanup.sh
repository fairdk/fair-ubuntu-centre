#!/bin/bash

echo "Clearing local apt cache"

rm -f /var/cache/apt/archives/*deb
