#!/bin/sh

# On distant machine

# Remove old network template
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 'rm -rf /home/debian/mi-lxc'
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && ./mi-lxc.py stop'"

# Destroy old netowork
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && echo y | ./mi-lxc.py destroy'"

# Export desired network
sshpass -p debian scp -r networks/$2 debian@$1:/home/debian/mi-lxc

# Copy network folder
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'rm -rf /root/mi-lxc'"
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cp -r /home/debian/mi-lxc /root/mi-lxc'"

# Make executable
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && find . -type f -iname \"*\" -exec chmod +x {} \;'"

# Create Network
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && chmod +x mi-lxc.py && ./mi-lxc.py create'"


sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && ./mi-lxc.py start'"
./user.sh $1 machine-home s3cr3t