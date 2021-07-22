#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

with open("/etc/bash.bashrc", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxloginpass-iOS/login.py", " ")
    file = open("/etc/bash.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/etc/bash.bashrc", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxloginpass-iOS/login-style.py", " ")
    file = open("/etc/bash.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()


with open("/etc/bash.bashrc", "r") as f:
    raw = f.read().lower().replace("chmod +x * && exit.sh", " ")
    file = open("/etc/bash.bashrc", "w")
    file.write(raw)
    file.close()
    f.close()


os.system("cd ~ && rm -rf ~/.linuxcolor ~/termuxloginpass")
