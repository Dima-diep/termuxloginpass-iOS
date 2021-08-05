#!/bin/bash
echo "#!/bin/bash" > /etc/login
echo "python3 ~/termuxloginpass-iOS/login.py" >> /etc/login
echo "python3 ~/termuxloginpass-iOS/login-style.py" >> /etc/login
mkdir ~/.linuxcolor
mv kalilinux ~/.linuxcolor
mv debian ~/.linuxcolor
mv Ubuntu ~/.linuxcolor
mv archlinux ~/.linuxcolor
