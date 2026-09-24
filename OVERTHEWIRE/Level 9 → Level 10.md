
# Bandit Level 9 → Level 10

>   **Platform:** OverTheWire **Game:** Bandit **Level:** 9-> 10 **Topic: The password for the next level is stored in the file **data.txt** in one of the few human-readable strings, preceded by several ‘=’ characters.

## GOAL: 
- Read the password by filtering the human-readable strings with preceded by serveral '='

# ANALYSIS: 
- As always I used the password for this level and login through SSH.
- After login I checked by giving command: `ls` and it lists me the file : ``data.txt.
- Now at this point as I know it's `.txt` file but also I like to check what type of file is this so I typed: `file file.txt` and from result I know that it contains data.
![](Attachments/Pasted%20image%2020260924170031.png)

 - Now I like to check what types of data it holdes so I typed: `head data.txt` and it give me some unreadble texts.
 - By playing multiple ctfs at this level I know that I can use a `String` command what data it holds.
 > The **`strings` command** in Linux is a command-line utility used ==to **extract and print human-readable text sequences from binary or non-text files**==

- So I typed: `string data.txt | grep "="`
- And then I got a flag, I give `grep "="` because from question we know that: the password is in preceded by several ‘=’ characters.
![](Attachments/Pasted%20image%2020260924170414.png)

- And the password for the next level i.e 10 is:
```text
B0s2khmbT9u0geKuOoVGW3JZKhndE3BG
```
