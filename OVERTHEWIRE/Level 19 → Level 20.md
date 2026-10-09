
# Bandit Level 19 → Level 20

> Platform:  Overthewire **Game**: Bandit level 19 -> 20  **Topic**: To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.


## GOAL: 
- Get the password for the next level in the file: `/etc/bandit_pass/bandit20`
- Also learn something on going on this about `suid` permissions in linux

## ANALYSIS: 
- As always I logged in with the previous level.
- And check the persmission on the file: `bandit20-do`
- This have the `s` in the user system so from here we know that it has an `setuid binary permission.`
![](Attachments/Pasted%20image%2020261009230624.png)

- If I execute that command it simply says that: `Run a command as another user`
![](Attachments/Pasted%20image%2020261009230924.png)
- So what I can do here is:
```bash
./bandit20-do whoami
```
![](Attachments/Pasted%20image%2020261009231139.png)
- So here we can see those commands are working
- Now, my work is to find the password file as question says that it's in the: `/etc/bandit_pass` let's see there.
![](Attachments/Pasted%20image%2020261009231245.png)
- Here, I can see the `bandit20` so let's try to view the content in this file.
```bash
./bandit20-do cat /etc/bandit_pass/bandit2
```
![](Attachments/Pasted%20image%2020261009231425.png)
- And here I can found the password for the next level:
```text
4pIjcunZ0fK2vmp3IwfG8Vf7VhxD6pOA
```