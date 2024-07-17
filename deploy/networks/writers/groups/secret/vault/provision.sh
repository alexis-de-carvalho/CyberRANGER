#!/bin/bash
set -e
if [ -z $MILXCGUARD ] ; then exit 1; fi
DIR=`dirname $0`
cd `dirname $0`

# systemctl set-default graphical.target

apt-get update
DEBIAN_FRONTEND=noninteractive apt-get install -y python3
DEBIAN_FRONTEND=noninteractive apt-get install -y python3-requests
DEBIAN_FRONTEND=noninteractive apt-get install -y gcc

apt install vsftpd

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
debian:vault!
EOF


sed -i 's/^anonymous_enable=.*/anonymous_enable=YES/' /etc/vsftpd.conf

systemctl restart vsftpd

echo 'A_b1t_m0r3_chall3ng1nG!!!' > /root/flag

echo 'Current novel is empty... We know it is disappointing, but we lack inspiration...' > /root/current_novel.txt

echo 'int main(int argc, char *argv[]) { setuid(0); system("cat /root/current_novel.txt"); }' > /home/debian/get_novel.c
gcc /home/debian/get_novel.c -o /home/debian/get_novel
rm /home/debian/get_novel.c
chmod u+s /home/debian/get_novel
