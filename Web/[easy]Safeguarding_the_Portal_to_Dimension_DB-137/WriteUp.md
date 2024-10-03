## Description

Rick Sanchez has been up to his usual mischief and built a highly vulnerable web application. In the pursuit of ultimate control, he’s hidden some sensitive admin details deep within the system. Your mission is to outsmart Rick’s lazily secured login system, bypass Morty’s paranoid warnings, and uncover Rick’s secret. But beware—Morty has tried to cover the tracks by creating a false sense of security.

## Hint
You'll need to dive into SQL injection and IDOR vulnerabilities to access the admin page and find the hidden password. Can you unlock the secrets hidden in Rick's code?


## Writeup

1) The login page is vulnerable to SQL Injection. admin' -- Leave the password field blank or add anything; it will be ignored. This logs you in as the admin because the condition always evaluates as true

2) The page of admin you will find will be the HoneyPot page, thus its not a actual admin page its dummy. After logging in, profiles can be accessed with URLs like /user?id=1. Change the id parameter in the URL to view other user profiles (e.g., /user?id=2). You won’t be able to view the admin profile, as it’s protected.

3) Now from the hints which were there in the different user's chats, its found that admin has a differnt login page name /admin_login

4) Now with the help of SQL injection, using a certain payload which is admin' or 1=1-- we can gain the admin access which redirects to the /admin_dashboard page.

5) The payload is hidden in plain site which can be seen with the help of source code.

## Flag
HTB{$QL_1sn't_that_h4rD}

## Author
Daksh Bhagwani
