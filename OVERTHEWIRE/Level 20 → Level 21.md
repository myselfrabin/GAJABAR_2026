
# Bandit Level 20 → Level 21

> Platform:  Overthewire **Game**: Bandit level 20 -> 21  **Topic**: There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). If the password is correct, it will transmit the password for the next level (bandit21).


## GOAL: 
- Use the netcat and send the previous level password and if it match then it will show the next level password


## ANALYSIS: 
- Ok I logged in into level 20 first and then there I can see: the file named: `suconnect`
- This `suconnect` file have the setuid permission.
- Now what I did this time was: I give an netcat command with:
```bash
echo 'Previous_level_pass' | nc -l -p <ANY_RANDOM_PORT_NUM> &
```
- The `&` is being used for: command needs to be run, but you don’t need to interact with it for a while and want to keep using the same terminal with other commands while the command is executing.

![](Attachments/Pasted%20image%2020261010152228.png)

- As we can see it's being done now let's see how can we execute the file `suconnect`
![](Attachments/Pasted%20image%2020261010152328.png)

- The process to do is: `./suconnect <PORT_NUMBER`
- Ok using that I got a next password.

![](Attachments/Pasted%20image%2020261010152448.png)

- The password for the next level is:
```text
bW9kBv5WC3P4yoDyf12LSdGuNz5ka6hY
```