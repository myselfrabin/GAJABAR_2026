# Bandit Level 18 → Level 19

> Platform:  Overthewire **Game**: Bandit level 18 -> 19  **Topic**: The password for the next level is stored in a file **readme** in the homedirectory. Unfortunately, someone has modified **.bashrc** to log you out when you log in with SSH.


## GOAL: 
- Find a way to login to the system if the `.bashrc` file is corrupted too.


## ANALYSIS: 
- Ok I tried simple login at first by using: 
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220
```
- And it shows:
![](Attachments/Pasted%20image%2020261009165125.png)

- Ok, it doesn't say password is wrong but it simply times out the connection and says bye bye cause the `.bashrc` file is corrupted here.
- One way to do this is: 
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
```
- Instead of logging into the machine with SSH, we execute a command through SSH instead. First, we use `ls` to make sure the readme file is in the folder then we can use `cat` to read it.
![](Attachments/Pasted%20image%2020261009170854.png)

- Now I can use `cat readme` to see what's in the readme file.
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```
![](Attachments/Pasted%20image%2020261009171000.png)

- And by this way we got the password for the next level i.e 
```text
KpsOfPkcP7i1FlIExk2QEjyt6dw8dxZI
```

## ANOTHER WAY TO SOLVE THIS
- We can also use the: `/bin/bash` as a command to spawn a bash shell with the `-t` flag, which allows a ‘pseudo-terminal’ to run on the target machine, this way we can run `\bin\sh`.
![](Attachments/Pasted%20image%2020261009171411.png)

- If we use -t flag then we have to use: /bin/sh if not then just /bin/bash would work.