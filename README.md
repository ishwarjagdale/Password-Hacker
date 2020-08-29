# Password-Hacker
Tries dictionary attacks for getting username and generates password from basic ascii letters and digit
https://hyperskill.org/projects/80

<img src="https://github.com/ishwarjagdale/Password-Hacker/blob/master/demonstration.gif" width="640" height="324"/>

## Syntax
```
hacking.py
```

## Stages
**Stage #1 Establishing a conncetion**  
For starters, let’s pretend the admin's website isn't protected at all. Learn how to connect to the server and receive data from it to access private information.

**Stage #2 Simple brute force**  
OK, the admin has pumped up the server and it is now password-protected. But the password is probably short. Let's hack it by applying brute force (and no, that does not mean taking a jackhammer to the physical server!).

**Stage #3 Smarter dictionary-based brute force**  
The admin has picked up on our attempts to access the server, so now it is protected with a more complex password. Maybe the password is long but not unique? Let's hack it using a dictionary of the most common passwords!

**Stage #4 Catching exception**  
The admin is really taking the case seriously. Now it is necessary to specify a valid login and password, and the password cannot be cracked by brute force. And yet, there is a vulnerability in the system that you can exploit to identify the admin's login and password.

**Stage #5 Time-based vulnerability**  
The admin has reacted quickly and made a patch that removes the vulnerability. It's time to look for another one. Poor admin…
