#!/bin/sh
set -e

VBOX="/usr/bin/VBoxManage"
VM_NAME="$1"
PATH="$2"

echo $VM_NAME 

"$VBOX" import "$PATH" --vsys 0 --vmname "$VM_NAME"
"$VBOX" modifyvm "$VM_NAME" --memory 1024
"$VBOX" modifyvm "$VM_NAME" --bridgeadapter1 ens33
"$VBOX" modifyvm "$VM_NAME" --nic1 bridged
"$VBOX" modifyvm "$VM_NAME" --nested-hw-virt on

exit 0
