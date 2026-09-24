
# Bandit Level 10 → Level 11

>   **Platform:** OverTheWire **Game:** Bandit **Level:** 10-> 11 **Topic: The password for the next level is stored in the file **data.txt**, which contains base64 encoded data

# GOAL: 
- The password is stored in the file `data.txt` but in the `base64` format decode it to see the original password.


## ANALYSIS: 
- Ok, I logged with the password for this level by using the ssh service.
- And then I used the `ls` command to view the file or folder and I found file called: `data.txt` there.
- And when I view the content of the `data.txt` it shows some unreadable data but at last it conatains `==` which leads me doubt into is it base64 encoded??
- Now I used the:
```bash
cat data.txt | base64 -d
```
- Using this command I can see the password basically what this does is: at first it list the content from the `data.txt` file and then pipe it and decoded that data using the command: `base64 -d`

![](Pasted%20image%2020260924172651.png)