
# Bandit Level 3 → Level 4

> **Platform:** OverTheWire **Game:** Bandit **Level:** 2 → 3 **Topic:** password for the next level is stored in a hidden file in the **inhere** directory.

---

## GOAL: 
- The password for the next level is stored in a hidden file in the **inhere** directory.

## ANALYSIS: 
- I opened the lab and run again the `ls` command and it shows me the `inhere` directory this time.
![[Pasted image 20260921081838.png]]

- And then I go into this folder by using the command `cd inhere`
- And inside the folder `inhere` when I type `ls` command I didnot find anything
- And when I used the command `ls -la` it shows me a file called: `...Hiding-From-You` 
- And now when I see the content of this file then I am able to get the password
![[Pasted image 20260921082127.png]]

- And the password is: 
```text
xzTXq1rDJQVVAzdv5cHq1TQytTWufAMq
```
