# Bandit Level 16 → Level 17

> Platform:  Overthewire **Game**: Bandit level 16 -> 17  **Topic**: The credentials for the next level can be retrieved by submitting the password of the current level to **a port on localhost in the range 31000 to 32000**. First find out which of these ports have a server listening on them. Then find out which of those speak SSL/TLS and which don’t. There is only 1 server that will give the next credentials, the others will simply send back to you whatever you send to it.



## GOAL: 
- Submit the password of the current level to the port on localhost and the port is between range: `31000 - 32000` find out which one speaks SSL/TLS and which don't and submit the password of current level which one speaks on that security levels.


## ANALYSIS: 
- As always I logged in with the previous level i.e level 16 here.
![](Attachments/Pasted%20image%2020261009152325.png)
- I am here at level 16
- Now this time I will be using the nmap between the port `31000 - 32000` to check which ports are opens and to know their version 
```bash
nmap -sV -sC -p 31000 - 32000 localhost -T4
```
- It will start to scan the localhost of the `bandit16`.
- And here I got two port i.e `31518` and `31790` as ssl service ports I will be further checking on this two ports.

![](Attachments/Pasted%20image%2020261009152842.png)

- Ok now on doing the research I got to know that: port `31518` is just a echo server so it will just repeat the input back to me.
- So the next option is to : connect to 31790 with an SSL-capable client
```bash
openssl s_client -connect localhost:31790 -quiet
```
- Now it gives me the placeholder to put the password.
![](Attachments/Pasted%20image%2020261009155600.png)
- After giving the password it gives me an `OPENSSH PRIVATE KEY`.
- Now I copied this key in my local machine and give only user permission and then hit the: 
```bash
ssh -i level17.key.private bandit17@bandit.labs.overthewire.org -p 2220
```
- This let's me login into the level 17
- And viewing the file: `/etc/bandit_pass/bandit17` I can see the password of next level there.

![](Attachments/Pasted%20image%2020261009155838.png)

- So the password for the next level i.e level 17 is:
```text
pWXMAZoxGC8JmDMfmT5MGEsobMM3vnj2
```

