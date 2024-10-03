#!/usr/bin/python3

flag = "****RETARDED****"

def encrypt(pt):
    return [((ord(i) ^ 0x41) << 8) for i in pt]

def decrypt(ct):
    # To be implemented
print(decrypt(ct))
