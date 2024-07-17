import os
import sys

ip = sys.argv[1]

os.system(f"sshpass -p debian ssh debian@{ip} 'cat > add.sh' < add.sh")
os.system(f"sshpass -p debian ssh debian@{ip} 'chmod +x add.sh'")
os.system(f"sshpass -p debian ssh debian@{ip} "printf '%s\n' 'root' | su -c 'cd /root/mi-lxc && ./mi-lxc.py start'"")
