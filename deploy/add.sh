#!/bin/sh

useradd --create-home $1
printf '%s\n%s\n' $2 $2 | passwd $1

echo "sudo sh -c 'chdir /root/mi-lxc && ./mi-lxc.py attach $1'" > /home/$1/connect.sh
chmod +x /home/$1/connect.sh

echo "\n$1 ALL=(ALL:ALL) ALL" >> /etc/sudoers

echo "\nMatch User $1\n	ForceCommand ./connect.sh\n" >> /etc/ssh/sshd_config
service ssh restart
