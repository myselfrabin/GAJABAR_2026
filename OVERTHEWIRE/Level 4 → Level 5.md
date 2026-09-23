
# BANDIT Level 4 → Level 5\

> **Platform:** OverTheWire **Game:** Bandit **Level:** 4 -> 5 **Topic:** find the password from the human readable file 



# GOAL: 
- Find the password from the human readable file.

## ANALYSIS: 
- I got the password for level 4 at previous lab so I used to login with that
- And when I do ls there were a *inhere* directory
- After I go into that directory again I do `ls` and saw there were a multiple files called: 
**-file00 -file01 -file02 -file03 ..............so on**
- So from the previous labs I know that `-` dashed treated as special in linux env so I need to use: `cat ./-file00` to view the content of the file00.
- So I tried to view that it shows some binary file that I don't even now
- And now this time I used to trick to see what type is that file by using: `file` command.
![[Pasted image 20260922220244.png]]

- Here we can see the `file07` is showing the ASCII text so it's human readable, so when I try to view that file content I can see the password.
![[Pasted image 20260922220346.png]]
- The password for the next level i.e 5 is: 
```text
6C7h9GD8M6ai5nr7wo1RonrzFjj9yIrG
```