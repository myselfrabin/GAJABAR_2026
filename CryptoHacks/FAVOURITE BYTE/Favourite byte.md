
---
For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.  
  
I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

```text
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
```
---
## GOAL: 
- The data is hidden in a single byte, where the secret is contained find out that secret


## ANALYSIS: 
- So reading the question we have a xored hex value and with a single byte
- In single byte there's 256 possible combination possible
- So we need to bruteforce that hex with each key
- At first we need to change that hex into bytes and then we'll be bruteforcing it.
![](Attachments/Pasted%20image%2020261017191617.png)

- On cyberchef I got flag for this challenge like this.
- I am right now using python and the key is `10` so I'm using that
![](Attachments/Pasted%20image%2020261017192044.png)
- At this point the flag `c` is only displayed because the how zip function works here it only take single bit value i.e 10 and not taking other
- To solve this I have to use `cycle iteration method in python`
- So for that I need to  import cycle first from the itertools`from itertools import cycle` and then use cycle function in the datakey place so that it will be iterate till the length of cipher.
![](Attachments/Pasted%20image%2020261017192532.png)

- And this is how I solved this challenge from python too.