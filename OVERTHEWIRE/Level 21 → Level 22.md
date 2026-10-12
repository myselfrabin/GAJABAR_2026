# Bandit Level 21 → Level 22

> Platform:  Overthewire **Game**: Bandit level 21 -> 22  **Topic**: A program is running automatically at regular intervals from **cron**, the time-based job scheduler. Look in **/etc/cron.d/** for the configuration and see what command is being executed.


## GOAL: 
- Look at the `/etc/cron.d` file and figure out next how to solve this lab.

## ANALYSIS: 
- As always I do logged in into the previous level with ssh and their password.
- And then I see the everyfile with : `ls -la /etc/cron.d` and it shows me: 
![](Attachments/Pasted%20image%2020261012234151.png)

- Now I will be looking for this file content by using `cat`, the command I will be using here is:
```bash
cat /etc/cron.d/cronjob_bandit22
```
- and it shows me:
![](Attachments/Pasted%20image%2020261012234418.png)
- Now I will be looking into what that file contains, for that I will be using:
```bash
cat /usr/bin/cronjob_bandit22.sh
```
![](Attachments/Pasted%20image%2020261012234615.png)

- Now from here I know that the password is being set into the file: `/etc/bandit_pass/bandit22` so the password has been appened into the /tmp folder so I'll be reading that file .
- And I got the password:
![](Attachments/Pasted%20image%2020261012235204.png)

- The password for the next level is:
```text
RYVux2rHEm9tiXHmLFzuR7Vhx6AZQMEz
```
