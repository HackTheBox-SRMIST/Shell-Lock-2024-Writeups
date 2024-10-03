
## Description

Can you get the flag out of it?

## Writeup

Once you download the file you will get a zip file, when extracting the zip it gives the error as -

![Screenshot 2024-09-28 180907](https://github.com/user-attachments/assets/f97be010-4934-4dd1-ac43-3cf765604a1a)

which means that the file is corrupted let's just fix with this command - zip -FF input.zip --out output.zip

![Screenshot 2024-09-28 181155](https://github.com/user-attachments/assets/bd246e0b-871f-4086-b8b8-ba412be79e80)

after successfully fixing the flag we get this image

![flag](https://github.com/user-attachments/assets/716701b5-3a01-4639-8986-af786aaebb47)


so its just a image generated using some binary digits, so lets jump on to dcode.fr
![Screenshot 2024-09-28 181510](https://github.com/user-attachments/assets/27e8a735-a4e9-4bbe-8fe1-0bc4290f8adb)

we got the binary data, lets just convert them to text
remove the extra 0 bits from the end

![Screenshot 2024-09-28 181732](https://github.com/user-attachments/assets/a18b1919-1bc9-46b1-8dc8-cecab5add2e0)

boom!! we got the flag

## Flag
HTB{FL46_QR_5C4NN3D}

## Author
Dhruv Gupta
