## 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d find the single byte secret from this data

from itertools import cycle

data = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'
key = '10'
## change into byte first

bytedata = bytes.fromhex(data)
bytekey = bytes.fromhex(key)
print(bytedata.decode())
print(bytekey)
## i need now result 
flag = bytes(a ^ b for a,b in zip(bytedata,cycle(bytekey)))
print(flag)
