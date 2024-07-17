#!/bin/bash
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# systemctl set-default graphical.target

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y python3
DEBIAN_FRONTEND=noninteractive apt-get install -y python3-requests
DEBIAN_FRONTEND=noninteractive apt-get install -y sudo

apt install ufw

cp -ar homedir/* /home/debian/
#ln -sf /home/debian/background.jpg /usr/share/images/desktop-base/default

# allow anyone, including "debian" used by hacker, to write into web root
chmod 777 /var/www/html

chown -R debian:debian /home/debian

# Disable DHCP and do DNS config
#sed -i "s/.*dhcp.*//" /etc/network/interfaces
#echo -e "domain internet.virt\nsearch internet.virt\nnameserver 10.0.0.1" > /etc/resolv.conf

# https://help.gnome.org/users/epiphany/stable/cert.html.en
# p11-kit : trust anchor /home/user/Downloads/certificate.crt


# update password debian
chpasswd << EOF
debian:S3cr3tT0k3n
EOF

echo 'debian ALL=(ALL:ALL) NOPASSWD:/usr/bin/vim /home/debian/short_novel.txt' >> /etc/sudoers

export PATH=/sbin:$PATH
ufw enable
ufw deny out ssh

echo 'For admin actions, you can access the router with the credentials root:s3cur3d_r0ut3r' > /root/README

echo 'Qu1t3_3a5Y!' > /root/flag
