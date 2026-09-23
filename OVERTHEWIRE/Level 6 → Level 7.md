
# Bandit  Level 6 → Level 7

> **Platform:** OverTheWire **Game:** Bandit **Level:** 6 -> 7 **Topic: The password for the next level is stored **somewhere on the server** and has all of the following properties:
> - owned by user bandit7
- owned by group bandit6
- 33 bytes in size




## ANALYSIS: 
- So I just logged in in to the challenge 6.
- And then I read Arch wiki blog on their page about linux users and groups related things.
- And now, there I read that we can search file by groupname means which group owns that file we can search that.
- The command for searching through group is:
```bash
find / -group _groupname_
```
- So as per my case: the groupname is: `bandit6`
- So I used the command as: 
```bash
find / -group bandit6
```
- And there I found a file called: `/bandit7.password` often viewing that file content I can see the password.
- The password for the level 7 is: 
```text
Bmnnvf82KzQlfxgAI2d1zYbr1u9pr3E3
```


![[Pasted image 20260922233522.png]]


- This is how I solved this lab.
- It will be disrespect for me If at this point If I don't fully read the linux user and group permission system and file system let's fully study that and only move to next level.