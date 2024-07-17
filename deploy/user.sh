#!/bin/sh

# Setup remote user for access
sshpass -p debian ssh debian@$1 "printf '%s\n' root | su -c './add.sh $2 $3' root"
