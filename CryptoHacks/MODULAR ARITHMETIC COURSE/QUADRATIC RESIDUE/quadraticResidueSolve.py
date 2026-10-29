'''
Given number to us: 
    p = 29 this is some prime number to us
    and the intergers are: 14 , 6 and 11.


    finding quadratic residue the relation is: x ^ 2 = c (mod p)

    we need to go till the p - 1 
    Now I need to find out here is: C 

    14 ^ 2 = 22  mod 29
    6 ^ 2 = 7 mod 29
    11 ^ 2 = 5 mod 29

'''
p = 29
ints = [14, 6, 11]

squares = {x: (x * x) % p for x in range(1, p)}   # x from 1 to p-1

for a in ints:
    roots = [x for x, c in squares.items() if c == a]
    print(a, roots)
