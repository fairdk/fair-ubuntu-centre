# Adding local overlays

The purpose of local overlays is to maintain and store configurations of
individual centre sites. So that upon support or visit to a school, all
configuration should be copied for later reference and made accessible for
reuse at other places.

In order to add a local overlay with executable files, create a directory,
for instance `my_local_overlay/` with the following content, all optional:

 - `my_local_overlay/postinstall/` - To be included in the postinstall.tar.gz
   that's sent to clients.
 - `my_local_overlay/filesystem/` - A filesystem overlay that's copied directly
   onto the installed server system's root path.
 - `my_local_overlay/install.sh` - A script that's executed if it exists.
