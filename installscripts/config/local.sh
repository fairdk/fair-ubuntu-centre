#/bin/bash

# This script interactively prompts about available local overlays and
# their install scripts.

postinstall_local="$SCRIPT_ROOT/postinstall/filesystem/local/"

echo "Removing old local overlays"
rm -rf $postinstall_local/*

for dir in `ls "$CONFIG_LOCAL"`
do
	if [ -d "$CONFIG_LOCAL/$dir" ]; then
		read -p "Do you want to use $dir ? [y/N] " yn
		if [[ ! $yn == "y" ]]; then echo "skipping"
		else
			if [ -d ${CONFIG_LOCAL}${dir}/filesystem ]
			then
				cp -rf ${CONFIG_LOCAL}${dir}/filesystem/* /
			fi
			if [ -f ${CONFIG_LOCAL}${dir}/install.sh ]
			then
				. ${CONFIG_LOCAL}${dir}/install.sh
			fi
			echo "Using $dir"
			postinstall_dir="${CONFIG_LOCAL}${dir}/postinstall/*"
			cp -rf $postinstall_dir $postinstall_local
		fi
	fi
done
