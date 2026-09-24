
# Bandit Level 7 → Level 8
> **Platform:** OverTheWire **Game:** Bandit **Level:** 7 -> 8 **Topic: The password for the next level is stored in the file **data.txt** next to the word **millionth**


## GOAL: 
- Find the file data.txt and from there find password which is stored next to the word **millionth**


## ANALYSIS: 
- I logged in into the bandit 7 using the password.
- And now I used the `ls` to view the file it shows me the `data.txt` file.
- And when I do : `cat data.txt` it shows so many of data which is impossible to read.
- So as I know the password is stored next to the word `millionth` so I decided to use grep there.
- The command I used to get the password is:
```bash
cat data.txt | grep millionth
```
- And it shows me the passsword.
![](./Attachments/Pasted%20image%2020260924095533.png)
- The password is: 
```text
VR1ljMayciFxbnUokuQmJFw6QC9VKtub
```
