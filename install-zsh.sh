#!/bin/bash
echo "python3 ~/termuxloginpass-iOS/login.py" >> /etc/zshrc
echo "chmod +x exit.sh && bash exit.sh" >> /etc/zshrc
echo "python3 ~/termuxloginpass-iOS/login-style.py" >> /etc/zshrc
mkdir ~/.linuxcolor
mv kalilinux ~/.linuxcolor
mv debian ~/.linuxcolor
mv Ubuntu ~/.linuxcolor
mv archlinux ~/.linuxcolor
