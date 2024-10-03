#!/usr/bin/python3

import os

key = os.urandom(4)
flag = b"***RETARDED****"

print([(flag[i] ^ key[i % 4]) for i in range(len(flag))])
