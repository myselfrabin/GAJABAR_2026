
# Bandit Level 11 → Level 12

> **Platform:** OverTheWire **Game:** Bandit **Level:** 10-> 11 **Topic: The password for the next level is stored in the file **data.txt**, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions
> 

## GOAL: 
- As the question specifies rotated by 13 position we need to decrypt the text using the ROT13 algorithm


## ANALYSIS:  
- As always I opened the lab and login using the ssh credentials I got in the previous challenge.
- Now, I typed the command: `ls` to see the files it shows me `data.txt`
- I want to see it's content so I use: `cat data.txt` and it shows me: 
![](Attachments/Pasted%20image%2020260924180434.png)

- And now I copied this text and went into the `cyberchef` to decrypt this text.
- Using `ROT13` algorithm to decrypt this text I got the password;
![](Attachments/Pasted%20image%2020260924180615.png)

- And the password for the next level i.e (12) is: 
```text
GROozWPO8QyN0mGrjUkID0WCYkZiQxrN
```

