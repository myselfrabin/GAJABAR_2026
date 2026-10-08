
  *Bandit Level 13 → Level 14**

> Platform:  Overthewire **Game**: Bandit level 14 -> 15  **Topic**: The password for the next level can be retrieved by submitting the password of the current level to **port 30000 on localhost**.


## GOAL : 
- Retrive the next password by submitting the current password on the port **30000** on localhost.

> Note: When we come across port and network somehow we need to go from the remote connection remember that too.

## ANALYSIS:
- As I logged in with the bandit level 14 with :
```bash
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
```
- And I got there password in the bandit_pass file on /etc folder.
- Now let me check first what service is running on the port 30000 cause this lab description talks about this port.
- For that I use an `nmap` the command is like:
```bash
nmap -sV -sC -p 30000 localhost
```
- And the result it gives is port 30000 is open and it's running `ndmps?` service.
![](Attachments/Pasted%20image%2020261007112107.png)

- Now the task is I need to submit this level password into the port `30000` in localhost 
- So, I can use a `netcat` for it
- The command would be:
```bash
nc host port
```
```bash
nc localhost 30000
```


![](Attachments/Pasted%20image%2020261007112348.png)

- And like this we get password for next level.
- The password is:
```text
pbLYuZtTg4MgaqfJx8jbA9gKKGqM68A7
```

