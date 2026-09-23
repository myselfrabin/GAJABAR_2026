# Bandit - Level 2 → 3

> **Platform:** OverTheWire **Game:** Bandit **Level:** 2 → 3 **Topic:** Reading files with spaces and double dashes in the name

---

## Goal

Read the password from a file called `--spaces in this filename--` located in the home directory.

---

## Commands Used

|Command|What it does|
|---|---|
|`ls`|Lists files and folders in the current directory|
|`cat -- '<filename>'`|Reads a file whose name starts with `--`, stopping shell from treating it as a flag|
|`cat './<filename>'`|Reads a file using a relative path, also works for tricky filenames|

---

## Why is This Filename Tricky?

This filename has two problems:

**Problem 1 - Double dash `--`** In Linux, `--` at the start of an argument tells the shell "stop treating what comes after as flags." So if you just run `cat --spaces in this filename--`, the shell tries to parse `--spaces` as an option flag and throws an error.

The fix is to put `--` before the filename in the command itself. This tells `cat` "everything after this double dash is a filename, not a flag":

```bash
cat -- '--spaces in this filename--'
```

**Problem 2 - Spaces in the name** Spaces normally separate arguments in a Linux command. So `cat --spaces in this filename--` looks like four separate arguments to the shell, not one filename. The fix is to wrap the filename in single quotes so the shell treats the whole thing as one argument.

---

## Solution

After logging in as `bandit2`, I ran `ls`:

```bash
bandit2@bandit:~$ ls
--spaces in this filename--
```

![[Pasted image 20260919125821.png]]

Running `cat` normally failed. After searching online I found two ways to read this file:

**Option 1 - Using `--` to stop flag parsing, and quotes for spaces:**

```bash
cat -- '--spaces in this filename--'
```

![[Pasted image 20260919130000.png]]

**Option 2 - Using a relative path (same trick as Level 1):**

```bash
cat './--spaces in this filename--'
```

Both gave the same result — the password for Level 3.

![[Pasted image 20260919130315.png]]

---

## Password

```
7ZZ2LFrykP2zEyvBl4m3clcL7tGYJPME
```

---

## Logging into Level 3

```bash
ssh bandit3@bandit.labs.overthewire.org -p 2220
```

---

## Key Takeaways

- **`--` in a command means "end of flags."** Anything after it is treated as a filename or argument, not a flag. This is the standard way to handle filenames that start with `-` or `--`.
- **Spaces in filenames need quoting.** Wrap the whole name in single quotes `'like this'` or escape each space with a backslash `like\ this`.
- **The relative path trick `./` works here too.** Just like Level 1 with the dash, prefixing with `./` forces the shell to treat it as a file path and avoids both the flag and space problems at once.
- **Two solutions is better than one.** Knowing multiple ways to solve the same problem means you're not stuck if one approach doesn't work in a different situation.

---

> **Previous:** [Bandit Level 1 → 2] **Next:** [Bandit Level 3 → 4](https://overthewire.org/wargames/bandit/bandit4.html)