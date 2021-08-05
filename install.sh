#!/bin/bash
echo "python3 ~/termuxloginpass-iOS/login.py" >> /etc/login
echo "chmod +x exit.sh && bash exit.sh" >> /etc/login
echo "python3 ~/termuxloginpass-iOS/login-style.py" >> /etc/login
mkdir ~/.linuxcolor
mv kalilinux ~/.linuxcolor
mv debian ~/.linuxcolor
mv Ubuntu ~/.linuxcolor
mv archlinux ~/.linuxcolor
