#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
import os

os.system("touch exit.sh")
os.system("echo \"#!/bin/bash\" > exit.sh")
os.system("echo \"exit\" >> exit.sh")
try:
    login = "oldlogin"
    print("Login:")
    a = input()

    if a == login:
        os.system("python3 ~/termuxloginpass-iOS/pass.py")
    elif a != login:
        print("Login incorrect")
        os.system("python3 ~/termuxloginpass-iOS/login.py")
except KeyboardInterrupt:
    os.system("python3 ~/termuxloginpass-iOS/login.py")
