

# Bandit Level 13 → Level 14

> Platform:  Overthewire **Game**: Bandit level 13 -> 14  **Topic**: The password for the next level is stored in **/etc/bandit_pass/bandit14 and can only be read by user bandit14**. For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. Look at the commands that logged you into previous bandit levels, and find out how to use the key for this level.  
If you need help with this level: a hint file can be found in the home directory.  
Make sure to read the error messages as they are informative.

## GOAL: 
- Logged in to the user bandit 14 via the private ssh key found in the user bandit 13
- After logged in with user 14 we can find the password for level 14 at file: `/etc/bandit_pass/bandit14` file.


## ANALYSIS:
- As always I logged in with the user `bandit13` via SSH.
- And when I see what files or folder it contain by giving `ls` it contains the `hint` and the `sshkey.private` file. 
![](Attachments/Pasted%20image%2020261006090149.png)

- Checking that file permission with `ls -la filename` the user bandit14 have the read and write permission and the group permission have with bandit13 user.
![](Pasted%20image%2020261006090653.png)

- Now what I can do here is: I can copy this sshkey.private file into my local device and from there try to login with this key file to the bandit user 14.
- Why? because this is own by an: user bandit14 and the server has an public key if it's correct then those key will matches and it let's us to login.
- The command I will be using for this is: 
```bash
ssh -i key.pem -p 2222 user@host
```

- Now I will be chaning it's file permission on my localhost why this? cause exceed file permission will give us SSH error so I will be only having a read and write permission on the user bandit14 and group and other permission I will be putting null at it.
![](Pasted%20image%2020261006091154.png)

- To do that I've use:
```bash
chmod 600 filename
```
- chmod is for chaning file permission and 600 is read + write permission on user and group or other permission will be removed here.
![](Pasted%20image%2020261006091629.png)
- So using the command: 
```bash
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```
- I get logged in into bandit14 user.
- Now as per question, If I see the file : `/etc/bandit_pass/banit14` I can see the password for the level 14

![](Pasted%20image%2020261006092000.png)

- The password for the next level is:
```text
aaWecNkG4FhxJQxz07uiwzVP6bJiYS65
```