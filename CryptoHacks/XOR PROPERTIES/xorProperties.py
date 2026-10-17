"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 
"""

key1= 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
## i need to take the key1 into bytes to perform xor

byteskey1 = bytes.fromhex(key1)
print(f"The key1 in bytes is:{byteskey1}")

## i have is: key2 ^ key1 = result
## as i know xor is self inversive i can find out the value of key2

key2Xoredkey1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')

key2 = bytes(a ^ b for a,b in zip(byteskey1,key2Xoredkey1))
print(f"The value of key2 is:{key2.hex()}")

## ok as i get key2 now what i have is: key2 ^ key 3 = result

key2Xoredkey3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')

key3 = bytes(a ^ b for a,b in zip(key2,key2Xoredkey3))
print(f"The value of key3 is: {key3.hex()}")

## as a final i have: flag ^ key1 ^ key3 ^ key2 = something

allxored = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

flag = bytes(a ^ b ^ c ^ d for a,b,c,d in zip(byteskey1,key2,key3,allxored))

print(flag.decode())


