
---
In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.  
  
There are four main properties we should consider when we solve challenges using the XOR operator.

Commutative: A ⊕ B = B ⊕ A  
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C  
Identity: A ⊕ 0 = A  
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.  
  
Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag
```text
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313  
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e  
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1  
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

> Before you XOR these objects, be sure to decode from hex to bytes.

---

## LET'S UNDERSTAND THE QUESTION AND FIGURE OUT WHAT TO DO: 
- I have series of output that is XOR'd together such as:
```text
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e 
```
- First let's try to figure it out what's value of `KEY2`??
	- KEY1= X
	- KEY 2 XOR'd X = Y 
	- so what's value of KEY2??
- Let's for try the `commutative property` for this one with expression: `x ^= y`
- One thing to note is XOR is `self-inverse` applying it twice with the same operand cancels out.
- so there result = x ^ z and z = x ^ result


## SO WHAT I DID TO SOLVE THIS LAB: 
- First of all, just know that the XOR is self inverse: a ^ b = result and If I need to find out value of a or b if any two of value result, a or b is given then I can find it out
- I follow the same principle for all of this.
- And what I notice is too: I can't perform xor(^) is string int like those kinds of thing I can only perform in the bytes also not whole one by one that is the reason I used `zip()` function there.
- And I can't see the string value if the decode will not support the `'utf-8'`, chaning it to latin-1 or anything won't work at all




![](Attachments/Pasted%20image%2020261017123424.png)