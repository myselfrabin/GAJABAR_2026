# Bandit Level 5 → Level 6

> **Platform:** OverTheWire **Game:** Bandit **Level:** 5 -> 6 **Topic:** The password for the next level is stored in a file somewhere under the **inhere** directory and has all of the following properties:
> - human-readable
- 1033 bytes in size
- not executable


ANALYSIS: 
- So I have previous last challenge password I login from there and now when I type `ls` it shows me an `inhere` directory
- And when I am into inside of that directory it shows me different folder such as: `maybehere` 
- So I knew the requirement of the file so I ran `find` command there by: 
```bash
find . -type f -size 1033c -exec bash {} \; | grep ASCII
```
- It shows me an result such as : 
```bash
find . -type f -size 1033c -exec bash {} \; | grep ASCII
./maybehere07/.file2: line 1: pXa26xhMWaC2SvDotA4r9EgZkulOeSBW: command not found
```
- But often searching I know I've got the password but this approach is not the correct one although I got an password through error when I use: bash there.
- And then I again use the:
```bash
find . -type f -size 1033c 
./maybehere07/.file2

```

- Ok at this point I know the password is stored inside the directory: `maybehere07` inside `.file2` remember the file name is: `dotfile2`
- So now this time when I see the content of `.file2` I can see the password with the bunch of spaces.

![[Pasted image 20260922231531.png]]

- The password for the level 6 is: 
```text
pXa26xhMWaC2SvDotA4r9EgZkulOeSBW
```
