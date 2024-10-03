## Description
I got a photo from my friend. He inserted a secret message in that picture. Can you help me find the message out?

https://drive.google.com/file/d/1iTlKo4BWo0pP3l8AenPmZElzfEIIAmLr/view?usp=sharing

## Writeup

First, we will use the basic analyzing tool “Binwalk” to check any file inside the jpg. 

![Screenshot 2024-09-24 133104](https://github.com/user-attachments/assets/0a313438-0041-4652-8f6d-f76c9bbf7ed8)

We can see that there is a compressed file named “text.txt” inside the image. 

To extract it we will use 7-zip. 

![Screenshot 2024-09-24 133412](https://github.com/user-attachments/assets/515b4f52-148d-45e2-b576-eeb652fe2da0)

We will now “cat” the txt file and there we found the flag.

![Screenshot 2024-09-24 133544](https://github.com/user-attachments/assets/14f097d0-ce67-4b09-8720-1e468be0df71)

## Flag
HTB{H3r3_i5_th3_f1ag}

## Author
Devansh Gupta

