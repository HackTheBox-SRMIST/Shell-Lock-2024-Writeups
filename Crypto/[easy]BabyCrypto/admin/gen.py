#!/usr/bin/python3

import os

key = os.urandom(4)
flag = b"HTB{Kn0wn_Pl4n3_73x7_4774ck}"

print([(flag[i] ^ key[i % 4]) for i in range(len(flag))])
