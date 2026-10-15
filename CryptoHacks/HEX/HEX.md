
---
platform: CryptoHack
category: HEX CODES
status: solved
tags:
  - python
  - crypto-basics
  - hex 
---




## QUESTION: 
---
When we encrypt something the resulting ciphertext commonly has bytes which are not printable ASCII characters. If we want to share our encrypted data, it's common to encode it into something more user-friendly and portable across different systems.  
  
Hexadecimal can be used in such a way to represent ASCII strings. First each letter is converted to an ordinal number according to the ASCII table (as in the previous challenge). Then the decimal numbers are converted to base-16 numbers, otherwise known as hexadecimal. The numbers can be combined together, into one long hex string.  
  
Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.  
  
```text
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```
---


## GOAL: 
- When we encrypt something into ciphertext it contains `bytes` which are not a printable ASCII codes.
- If we want a encrypted data, it's common to encoded it into something more user-friendly.
- For that we can use the hexadecimal to represent the ASCII string.
- At first we convert each letter to an ordinal number according to ASCII table, and that decimal number are converted to base-16 numbers, i.e the hexadecimal numbers.
- Those numbers can combine together, into one long hex string.
- There's a encoded hex string, we need to decode that to get the flag.

## ANALYSIS: 
- The given string was the encoded hex
- Now I decode it with the `bytes.fromhex()` and then I got the flag for this challenge




![](Attachments/Pasted%20image%2020261015100939.png)
