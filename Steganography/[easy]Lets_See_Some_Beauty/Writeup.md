## Description
Petrov told me I can simply go ahead and see the flag...All I see are 4 files without extension. Can you unravel the secret for me

## Writeup
You were provided the following 4 files -

https://drive.google.com/drive/folders/1Bmm3C9THpGJrM0HREa61siYWF99Y9rGw

Hint was in the question's description "petrov"

A simple google search petrov will lead you to the following tool - https://github.com/DimitarPetrov/stegify

just use the decode command provided in the documentation to reveal the flag :)

`stegify decode --carriers "1111111 2222222 3333333 4444444" --result flag.png`
![image](https://github.com/user-attachments/assets/2931c906-1334-448c-8379-8ed0bbb528b1)


output ->
![image](https://github.com/user-attachments/assets/08136940-76c4-4db0-b378-5af8a5b792b0)

## Flag
HTB{wee_woo_wee_woo}

## Author
Jayesh Gaba



