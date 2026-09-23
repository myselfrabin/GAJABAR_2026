# Bandit - Level 1 → 2

> **Platform:** OverTheWire **Game:** Bandit **Level:** 1 → 2 **Topic:** Reading files with dashed names

---

## Goal

Read the password from a file named `-` (a single dash) and use it to log into Level 2.

---

## Commands Used

|Command|What it does|
|---|---|
|`ls`|Lists files and folders in the current directory|
|`cat ./-`|Reads a file named `-` using a relative path|

---

## Why is a Dashed Filename Tricky?

In Linux, a single dash `-` is treated as a special symbol by the shell. When you run `cat -`, the shell doesn't look for a file called `-` — instead it interprets `-` as "read from keyboard input" (stdin). So it just hangs there waiting for you to type something, which is not what we want.

The fix is to give it a **relative path** instead of just the filename. Adding `./` before the dash tells the shell: "this is a file in the current directory called `-`", not a special flag.

```bash
cat ./-       # correct - reads the file
cat -         # wrong - waits for keyboard input
```

---

## Solution

After logging in as `bandit1`, I ran `ls` to check what files were there:

```bash
bandit1@bandit:~$ ls
-
```

Just one file with the name `-`.

![[Pasted image 20260919105719.png]]

Trying `cat -` didn't work — it just hung waiting for input. After a quick search I found the relative path trick:

```bash
bandit1@bandit:~$ cat ./-
```

![[Pasted image 20260919105919.png]]

This printed the password for Level 2.

![[Pasted image 20260919110020.png]]

---

## Password

```
PK8fYLZg2hnHSz83plBL1iEPKdD3QToB
```

---

## Logging into Level 2

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
```

Login successful  changed to `bandit2@bandit`.

![[Pasted image 20260919110212.png]]

---

## Key Takeaways

- **`-` means something special to the shell.** It usually means "use standard input" rather than a file. Any time a filename looks like a flag or symbol, you need to be careful about how you reference it.
- **`./` forces the shell to treat the name as a file path.** You can also use the full path like `/home/bandit1/-` — both work the same way.
- **When a command behaves unexpectedly, search why.** Looking up "how to read a file named dash in Linux" is exactly the right move — this is a real skill, not cheating.

---

> **Previous:** [ **Next:** [Bandit Level 2 → 3](https://overthewire.org/wargames/bandit/bandit3.html)