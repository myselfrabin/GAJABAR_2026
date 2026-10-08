
- We'll be install it via the cargo
- The command for installation is:
```bash
curl --proto '=https' --tlsv1.2 -sSf [https://sh.rustup.rs](https://sh.rustup.rs/) | sh
```


## AFTER THAT Load the new PATH in CURRENT TERMINAL: 
```bash
source "$HOME/.cargo/env
```

- And then I can see it's version: 
```bash
rustc --version
```

![](Attachments/Pasted%20image%2020261008122450.png)

- I also can see it via the `rustrc` version
```bash
cargo --version
```
![](Attachments/Pasted%20image%2020261008122604.png)

