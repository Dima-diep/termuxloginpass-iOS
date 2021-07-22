#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os
import getpass

try:
    #password have to be as a single word in " "
    passwd = "oldpass"
    a = getpass.getpass("Password: ")

    if a == passwd:
        os.system("rm -rf exit.sh")
        os.system("neofetch")
    elif a != passwd:
        print("Password incorrect")
        os.system("rm -rf exit.sh")
        os.system("python3 ~/termuxloginpass-iOS/login.py")
except KeyboardInterrupt:
    os.system("python3 ~/termuxloginpass-iOS/login.py")
