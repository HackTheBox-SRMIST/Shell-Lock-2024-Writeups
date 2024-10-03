## Description

While I was working on encryption, my friend took control of my computer and encrypted some files -_- Could you please assist me?

👧🐴🐭🐨

564ac7122cf386adfdde2d119f06b8609211e2a131f919b184d12bbb00cd606c

;3'/

\u0064\u003d\u0032\u0034\u0031\u0033\u0039

8895,8548,3157,7626,10408,9493,637,5438,10502,9493,5438,10313,3952,7851,5438,11898,3952,10408,5438,2945,10138,2945,10408,9942,3952,10313,2945,10411



## Writeup

The first string seems to be a base100 emoji cipher after some basic google searches. Translating it we get,

p=61

coming to the second string, looks like its a SHA256 hash. Decrypting it...

564ac7122cf386adfdde2d119f06b8609211e2a131f919b184d12bbb00cd606c : Q197

Third one seems to be random characters. decrypting the string using ROT47 and then using ascii shift, we find:

E=19

finally the last string seems to simply be Unicode. It reads:

d=24139

so we have the values of p, q, e and d.

No we can just use an RSA calculator, put these values and get the answer by running the ciphertext through it. We get the flag!

## Flag
HTB{r54_i5_n0t_f0r_3v3ry0n3}


## Author
Utkarsh Jaiswal







