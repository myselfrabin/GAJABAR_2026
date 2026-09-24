
# Bandit Level 8 → Level 9

>  **Platform:** OverTheWire **Game:** Bandit **Level:** 8-> 9 **Topic: The password for the next level is stored in the file **data.txt** and is the only line of text that occurs only once.


# GOAL: 
- Get the only unique list of line of text that is password in this case.

## ANALYSIS: 
- As always I logged in with the level 8 using `ssh`.
- And now I view the files with the `ls` it shows the file `data.txt`
- Seeing the file content it shows so many of lines.
- And When I read the challenge description it clearly says the line of text that occurs only once.
- So to get that only one time coming single line of text I used mixed of commands i.e `sort` and `unique`.
- The command I used to get the password is: 
```bash
sort data.txt | uniq -u
EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl
```
- Here the `sort` command will rearrange the content in the file and the uniq will show only unique lines of text but with the `-u` flag it shows only one time occuring unique lines this is how we get the password.
![](./Attachments/Pasted%20image%2020260924102105.png)

- The password for the next level is: 
```text
EjmOSvuAu7sGAHqHVcBDPirRe9T03kxl
```