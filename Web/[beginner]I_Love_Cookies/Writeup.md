## Description
Morty recently learned about base64 encoding. He tried logging into a website but got the user access. Help him to get admin access

Username: John

Password: john123


## Writeup

1) When you login with the creds available in the question, while inspecting the cookies you can see a Base64 encoded string.
2) On decoding it gives the username which is "John"
3) In order to get the admin access, encode admin string in Base64 and replace the cookies
4) You will get the flag.

## Flag
HTB{AdM1N_4c3s$_GraNt3d}

## Author
Daksh Bhagwani
