
---
We've looked at multiplication and division in modular arithmetic, but what does it mean to take the square root modulo an integer?

For the following discussion, let's work modulo p=29. We can take the integer a=11 and calculate a^2=5mod  29.

As a = 11 , a^2 = 5 , we say the square root of 5 is 11.

This feels good, but now let's think about the square root of 18. From the above, we know we need to find some integer a such that a^2=18

Your first idea might be to start with a=1 and loop to a=p−1. In this discussion p isn't too large and we can quickly check all options.

  
Have a go, try coding this and see what you find. If you've coded it right, you'll find that for all a∈Fp∗​ you never find an a such that a^2=18.

What we are seeing, is that for the elements of Fp∗, not every element has a square root. In fact, what we find is that for roughly one half of the elements of Fp∗​, there is no square root.

> We say that an integer x is a _Quadratic Residue_ if there exists an a such that a2≡xmod  p. If there is no such solution, then the integer is a _Quadratic Non-Residue_.

In other words, x is a quadratic residue when it is possible to take the square root of x modulo an integer p.

In the below list there are two non-quadratic residues and one quadratic residue.
Find the quadratic residue and then calculate its square root. Of the two possible roots, submit the smaller one as the flag.

>If a^2=x then (−a)^2=x. So if x is a quadratic residue in some finite field, then there are always two solutions for a.

> p=29           ints=[14,6,11]


---


## SOME RESEARCH:
### SQUARE ROOT OF AN MODULAR INTERGER:
- Let p = 29 and a = 11 and if we calculate: a^2 === 5 mod 29 in this case we can say that the square root of 5 is 11.

## WIKI: 
- In number theory, **an integer q** is a **quadratic residue** modulo n if it's **congruent** to a **perfect square** modulo n; that's if there exist an integer x such that:
```text
x^2 = q (mod n).
    =
    =
```


## SO WHAT'S CONGRUENT?
- A given positive integer n, two intergers a and b are called congruent modulo n, written if:
$$a \equiv b \pmod{n}$$

- if a - b is divisible by n.

> In normal math, the square root of 18 is decimal (~ 4.24). But in modular math, we only care about whole numbers.
> The goal is to find a whole number a (between 1 and p-1) that satisfies:
> 	a ^ 2 (mod p ) = 18



## ALGORITHM FOR THIS CHALLENGE: 
1. Start at a = 1
2. Calculate: a ^2 (mod p)
3. Check if the result equals to 18
4. If not move to a= 2 then a = 3 all the digits up to p - 1.




## FINDING THE QUADRATIC RESIDUE AS PER QUESTION: 

- ```text
  p=29  ints=[14,6,11]
  ```
