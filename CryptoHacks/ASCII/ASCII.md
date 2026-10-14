---
platform: CryptoHack
category: ASCII CODES
status: solved
tags:
  - python
  - crypto-basics
  - ASCII
---
ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.  
  
Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.  
  
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]  
  
In Python, the `chr()` function can be used to convert an ASCII ordinal number to a character (the `ord()` function does the opposite).


## SOME RESEARCH AND THEORY OF MY OWN: 
- ASCII is a encoding system that assign unique numerical values to letters, digits , punctuation marks and control codes.
- It uses `7-bit binary number` that represent the `128` distinct characters including english alphabets , numerals , and basic symbols.
- We use ASCII in computers because it provides a **universal standard** that allows different electronic devices and systems to communicate seamlessly.
- Since computers only process binary data (0s and 1s), ASCII acts as a critical bridge, translating human-readable text into machine-readable numeric codes and vice versa.


## ANALYSIS: 
- I will be using python to solve this.
- I've used chr() function in python to change the numbers into character
- And using that prints me the flag.

![](Attachments/Pasted%20image%2020261014223539.png)


