#!/bin/sh
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential python-dev-is-python3 python3-pip libffi-dev sshpass curl virtualbox ansible
pip install -r requirements.txt
