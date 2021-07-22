#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

print("Old login:")
a = input()
print("New login:")
b = input()

with open("~/termuxloginpass-iOS/login.py", "r") as f:
    raw = f.read().lower().replace(a, b)
    file = open("~/termuxloginpass-iOS/login.py", "w")
    file.write(raw)
    file.close()
    f.close()
