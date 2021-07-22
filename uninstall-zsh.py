#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

with open("/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxlogin-iOS/login.py", " ")
    file = open("/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("python3 ~/termuxlogin-iOS/login-style.py", " ")
    file = open("/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

with open("/etc/zshrc", "r") as f:
    raw = f.read().lower().replace("chmod +x * && bash exit.sh", " ")
    file = open("/etc/zshrc", "w")
    file.write(raw)
    file.close()
    f.close()

os.system("cd ~ && rm -rf ~/.linuxcolor ~/termuxloginpass")
