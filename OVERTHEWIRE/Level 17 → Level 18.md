# Bandit Level 17 → Level 18

> Platform:  Overthewire **Game**: Bandit level 16 -> 17  **Topic**:There are 2 files in the homedirectory: **passwords.old and passwords.new**. The password for the next level is in **passwords.new** and is the only line that has been changed between **passwords.old and passwords.new**



## GOAL: 
- Compare the two files and find the password that has been changed from the old one.


## ANALAYSIS: 
- Ok I am into the bandit17 homepage when I do the `ls` I can see there are two files they are:
![](Pasted%20image%2020261009161934.png)

- Now I can use `diff` command to compare this two files.
```bash
diff passwords.new passwords.old -c
```

![](Attachments/Pasted%20image%2020261009162422.png)

- So the old and new passwords are:
```text
OQxXZjELndr90zuhOTDYBEomI0SZITXI        --> new
z7vPcsOPfFxnloUxixqYv4aWHUrx49K6        --> old
```

