#/bin/bash

if [ -n "${SCRIPT_ROOT}" ]; then
	""
else
        SCRIPT="`readlink -e $0`"
        SCRIPTPATH="`dirname $SCRIPT`"
        export SCRIPT_ROOT=$SCRIPTPATH/..
        . $SCRIPTPATH/../config/default_cfg.sh
fi

postinstall_local="$SCRIPT_ROOT/postinstall/filesystem/local/"

echo "---------------------------------------"
echo "Adding local overlay                   "
echo "---------------------------------------"

echo "Removing old local overlays"
rm -rf $postinstall_local/*

for dir in `ls "$CONFIG_LOCAL"`
do
	if [ -d "$CONFIG_LOCAL/$dir" ]; then
		read -p "Do you want to use $dir ? [Y/n] " yn
		if [ $yn == "n" ]; then echo "skipping"
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



