# Bandit - Level 0 → 1

> **Platform:** OverTheWire **Game:** Bandit **Level:** 0 → 1 **Topic:** Reading a file in Linux

---

## Goal

Find the password stored in a file called `readme` in the home directory, then use it to log into Level 1.

---

## Commands Used

|Command|What it does|
|---|---|
|`ls`|Lists files and folders in the current directory|
|`cat <filename>`|Prints the contents of a file to the terminal|

---

## Solution

After logging in as `bandit0`, I ran `ls` to see what files were in the home directory:

```bash
bandit0@bandit:~$ ls
readme
```

There was one file called `readme`. I read its contents using `cat`:

```bash
bandit0@bandit:~$ cat readme
```

This printed the password for Level 1.

![[Pasted image 20260919102354.png]]

---

## Logging into Level 1

With the password from the `readme` file, I connected to the next level:

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
```

When prompted, I entered the password from the file. Login was successful  the prompt changed to `bandit1@bandit`.

![[Pasted image 20260919103310.png]]

- This is the password we got here: `6y2kwnwK6grgvwvpvLaa2T1cpFEKOhNR`
---

## Key Takeaways

- **`ls` shows you what's in the current directory.** Always the first thing to run when you land on a new level — you need to know what you are working with.
- **`cat` reads a file and prints it to the screen.** Simple but one of the most used commands in Linux.
- **Each level's password unlocks the next SSH session.** The username changes (`bandit0` → `bandit1`) but the host and port stay the same throughout the game.

---

> **Previous:** [LEVEL-s0] **Next:** [Bandit Level 2](https://overthewire.org/wargames/bandit/bandit2.html)