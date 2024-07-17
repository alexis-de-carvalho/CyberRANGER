#!/bin/sh

# Destroy the network
VBoxManage controlvm "$1" poweroff
VBoxManage unregistervm "$1"
rm -rf ~/VirtualBox\ VMs/$1