#!/bin/sh

# Start the network
sshpass -p debian ssh -o StrictHostKeyChecking=no debian@$1 "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && ./mi-lxc.py start'"
