## Description 

You’ve just been hired as a cybersecurity analyst for a marine research institute, and on your first day, you're given an unusual case. A group of marine biologists were tracking great white sharks off the coast when one of their servers was breached. They suspect someone embedded a hidden message inside one of their network data files.

You’re handed a pcapng file—a network capture from the compromised server. The team believes a password is concealed within the data, possibly hidden among the sharks’ telemetry data.

Your mission: Analyze the pcapng file and find the answers we have been looking for.

File: https://drive.google.com/file/d/1Y6TYWDKKJzQybbebQoHyJYCM4ly6Dg8T/view?usp=sharing

## Writeup

Now the file consists of may different packet namely TCP,NTP,DNS,HTTP and many more.

There are many packets in the file and it is very difficult to find the flags on its own so we try to check the different streams of different packets.

So first we check the tcp streams.

So there is no luck over here.

![Screenshot_20240921_002132](https://github.com/user-attachments/assets/62305944-74ea-4f37-997e-f1dbd5ff9798)

But I do notice that there are many packets with many http requests which can show some promise on results.

So i check http requests and notice that there are many login.php requests and hence there were login attempts made on a http site which can be unsafe and provide us with some clear text passwords.

![Screenshot_20240921_004008-1](https://github.com/user-attachments/assets/550c65c8-a19a-479e-8c5d-6b1c81916174)

So we check all the streams conntaining http. And get something interesting...

![Screenshot_20240921_004223](https://github.com/user-attachments/assets/32b41206-d5cd-4e94-9182-566198f9d6b3)

So if we continue this path i believe we will get the flag..

And We find the flag.

![Screenshot_20240921_004423](https://github.com/user-attachments/assets/3bf05141-24ff-4750-b23b-a48901a25d87)

the flag is encrypted with ROT so after decryption we get the flag!


## Flag
`HTB{TH!$_!S_$3R!OU$LY_UNS4F3}`


## Author
DHRUV PRIDHNANI
