
# Bandit Level 15 → Level 16

>Platform:  Overthewire **Game**: Bandit level 15 -> 16  **Topic**: The password for the next level can be retrieved by submitting the password of the current level to **port 30001 on localhost** using SSL/TLS encryption.
**Helpful note: Getting “DONE”, “RENEGOTIATING” or “KEYUPDATE”? Read the “CONNECTED COMMANDS” section in the manpage.**



## GOAL: 
- Submit the password of current level to the port `30001` on the localhost using the SSL/TLS encryption.


## ANALYSIS:
- As always I logged in with the previous level i.e level 15 in this case.
- And then the to do work for this level is we need to submit the password to port `30001` on localhost with SSL/TSL encryption
- We can do this via the `openssl` the command would look like:
```bash
openssl s_client -connect localhost:30001
```
- And after that it asks me for the previous level password after giving that we get the password for the next level.
![](Attachments/Pasted%20image%2020261009132924.png)

- The password for the next level is:
```text
kS0Hf0u5HiXFwKMKFqXvPdOTNGGa0X8V
```