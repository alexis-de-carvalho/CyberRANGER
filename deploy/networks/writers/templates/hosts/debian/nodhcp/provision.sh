#!/bin/sh
# nodhcp template
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# systemctl set-default graphical.target

DEBIAN_FRONTEND=noninteractive apt-get install -y nmap

# Disable DHCP and do DNS config
#sed -i "s/.*dhcp.*//" /etc/network/interfaces
sed -i "s/dhcp/manual/" /etc/network/interfaces
echo "domain $domain\nsearch $domain\nnameserver $ns" > /etc/resolv.conf


# update password root
chpasswd << EOF
root:0utland3R
EOF
