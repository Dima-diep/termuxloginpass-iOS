#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

a = "kali"

if a == "arch":
    os.system("cat ~/.linuxcolor/archlinux | lolcat -S 65 -a -s 40 -i")
elif a == "debian":
    os.system("cat ~/.linuxcolor/debian | lolcat -S 40 -a -s 40 -i")
elif a == "kali":
    os.system("cat ~/.linuxcolor/kalilinux | lolcat -S 55 -a -s 40 -i")
elif a == "ubuntu":
    os.system("cat ~/.linuxcolor/Ubuntu | lolcat -S 30 -a -s 40 -i")
