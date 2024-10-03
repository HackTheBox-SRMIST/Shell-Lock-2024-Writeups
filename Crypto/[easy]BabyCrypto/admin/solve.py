#!/usr/bin/python3

a = [7, 71, 189, 96, 4, 125, 207, 108, 33, 76, 175, 119, 123, 125, 204, 68, 120, 32, 135, 44, 16, 39, 200, 44, 123, 112, 148, 102]

key = [(i ^ k) for i,k in zip(a,b"HTB{")]
print(''.join([chr(a[k] ^ key[k % 4]) for k in range(len(a))]))
