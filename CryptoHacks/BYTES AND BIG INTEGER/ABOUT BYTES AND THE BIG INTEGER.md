

Cryptosystems like RSA works on numbers, but messages are made up of characters. How should we convert our messages into numbers so that mathematical operations can be applied?  
  
The most common way is to take the ordinal bytes of the message, convert them into hexadecimal, and concatenate. This can be interpreted as a base-16/hexadecimal number, and also represented in base-10/decimal.  
  
To illustrate:
```text
message: HELLO  
ascii bytes: [72, 69, 76, 76, 79]  
hex bytes: [0x48, 0x45, 0x4c, 0x4c, 0x4f]  
base-16: 0x48454c4c4f  
base-10: 310400273487
```

> Python's PyCryptodome library implements this with the methods `bytes_to_long()` and `long_to_bytes()`. You will first have to install PyCryptodome and import it with `from Crypto.Util.number import *`.


## SOME RESEARCH ON THIS TOPIC BEFORE SOLVING THE LAB: 
To convert a message into a number for cryptography in Python, you should encode the text into bytes and then interpret those bytes as a large integer. This method ensures that the entire message is represented as a single numeric value suitable for algorithms like RSA.

**Recommended Method: `int.from_bytes()`**  
The most robust and standard approach in Python is to use the `int.from_bytes()` function on the encoded string. This handles character encoding (typically UTF-8) and byte ordering correctly.
```python
def string_to_int(message):
    # Encode the string to bytes, then convert to an integer
    # 'big' endian is standard for cryptographic representations
    return int.from_bytes(message.encode('utf-8'), byteorder='big')

# Example
message = "Hello"
number = string_to_int(message)
print(number)   
```

**Alternative Method: Block Integer Conversion**  
For public key ciphers like RSA that operate on fixed-size blocks, you can convert a string into a block integer by treating characters as digits in a base corresponding to the symbol set size. 

1. Define a **symbol set** (e.g., uppercase letters, lowercase letters, digits).
    
2. For each character, find its index in the symbol set.
    
3. Multiply the index by the base raised to the power of the character's position within the block.
    
4. Sum these values to get the block integer.
```python
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
BASE = len(SYMBOLS)

def string_to_block_int(message, block_size):
    block_int = 0
    for i, char in enumerate(message):
        if char in SYMBOLS:
            index = SYMBOLS.index(char)
            # Position within the block (0 for first char, 1 for second, etc.)
            pos = i % block_size
            block_int += index * (BASE ** pos)
    return block_int   
```

**Reversing the Conversion**  
To convert the number back to text, use `int.to_bytes()` for the first method or modulo and floor division for the block method.
```python
import math

def int_to_string(number, length=None):
    if length is None:
        # Calculate minimum bytes needed
        length = math.ceil(number.bit_length() / 8)
    # Convert integer back to bytes, then decode to string
    return number.to_bytes(length, byteorder='big').decode('utf-8')   
```


## ANALYSIS: 
- I will be doing the first method here.
- Ok after using the `long_to_bytes` it works as I expected but why is the question?

## LONG_TO_BYTES:
- `long_to_bytes(n)` converts the `large interger` into a `byte string`.
- Also we can use: `bytes_to_long(s)` convert a byte string into the long interger.
- By using this and coding in the python I solved this lab.

![](Attachments/Pasted%20image%2020261016140458.png)