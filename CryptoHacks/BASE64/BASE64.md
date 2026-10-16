
---
Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.  
  
Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.  
  
Take the below hex string, _decode_ it into bytes and then _encode_ it into Base64.

```text
72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
```

---


## GOAL: 
- We have given a hex String firstly we need to decode that into bytes and then and after that we need to encode that into the base64.

## ANALYSIS: 
- Ok I do first decode that string into hex by: `bytes.fromhex()`
- And then I encoded that into the base64 by using: `base64.b64encoded()`
- And then I got the flag for this challenge
```text
crypto/Base+64+Encoding+is+Web+Safe/
```


![](Attachments/Pasted%20image%2020261016084617.png)


## NOTE FROM THIS LAB: 
- `bytes.fromhex(hexString)` converts hexadecimal text into raw bytes.
    
- `base64.b64encode(byte_data)` encodes those bytes into Base64.