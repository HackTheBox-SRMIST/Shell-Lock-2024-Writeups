## Description

Random is always safe, You Know?

## Writeup

We were given two files; the first is the Python program used to convert the flag into the encrypted text, and the output of that Python file is in out.txt.

chall.py :-
```python
#!/usr/bin/python3

import os

key = os.urandom(4)
flag = b"***RETARDED****"

print([(flag[i] ^ key[i % 4]) for i in range(len(flag))])
```

out.txt :-
```
[7, 71, 189, 96, 4, 125, 207, 108, 33, 76, 175, 119, 123, 125, 204, 68, 120, 32, 135, 44, 16, 39, 200, 44, 123, 112, 148, 102]
```



Analyzing the code, we can see the following:

--> First, It generates 4 random bytes.

--> Then, It Xor's the entire flag with the same 4 bytes

--> Then, It prints the output, which is our out.txt

## Exploit Path's

--> Who care about random bytes, can't we just bruteforce 4 bytes? :)
  - Bruteforcing 4 bytes is 4294967296 possibilites, which should be doable with given time.
  - But.... XOR provides many many close flags as it gets closer to the random key and it would be a real pain to try all the close flags and see which one is correct

--> Next, Trying to recover the key
  - We know, key ^ pt = ct and ct ^ pt = key
  - We know the first 4 bytes of the flag, which is just format "HTB{"
  - Knowing that, we XOR with the given cipher text to recover all 4 bytes of the KEY
  - Then, we finally XOR the cipher text with the recovered key to get the flag :)

solve.py :
```
a = [7, 71, 189, 96, 4, 125, 207, 108, 33, 76, 175, 119, 123, 125, 204, 68, 120, 32, 135, 44, 16, 39, 200, 44, 123, 112, 148, 102]

key = [(i ^ k) for i,k in zip(a,b"HTB{")]
print(''.join([chr(a[k] ^ key[k % 4]) for k in range(len(a))]))
```

## Flag

**HTB{Kn0wn_Pl4n3_73x7_4774ck}**

## Author
Sai Shashank

