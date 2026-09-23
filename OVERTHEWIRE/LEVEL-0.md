# Bandit - Level 0

> **Platform:** OverTheWire **Game:** Bandit **Level:** 0  **Topic:** SSH basics

---

## Goal

Log into the Bandit game server using SSH with the credentials provided.

```
Host     : bandit.labs.overthewire.org
Port     : 2220
Username : bandit0
Password : bandit0
```

---

## What is SSH?

SSH (Secure Shell) is a way to remotely connect to another computer over a network and control it through the terminal. It's encrypted, meaning no one can read what's being sent between your machine and the server.

The basic syntax is:

```bash
ssh <username>@<host> -p <port>
```

- `username` - who you are logging in as
- `host` - the address of the server
- `-p` - the port to connect on (default SSH port is 22, but this server uses 2220)

---

## Solution

Open a terminal and run:

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
```

When prompted for a password, enter:

```
bandit0
```

If the login is successful, your terminal prompt changes from your own machine's name to the bandit server:

```
bandit0@bandit:~$
```

That change in the prompt  from `rakshak07@kali` to `bandit0@bandit` confirms you are now inside the remote server.

![[Pasted image 20260919100538.png]]

---

## Key Takeaways

- **SSH lets you control a remote machine through your terminal.** You are not on your own computer anymore once the prompt changes.
- **Port matters.** The default SSH port is 22. This server runs on 2220, so the `-p 2220` flag is required or the connection will fail silently.
- **`username@host` is the standard format.** Forgetting the username before `@` means the server doesn't know which account to log you into.

---

> **Next:** [Bandit Level 1](https://overthewire.org/wargames/bandit/bandit1.html)