
---
We'll pick up from the last challenge and imagine we've picked a modulus `p`, and we will restrict ourselves to the case when `p` is prime.

The integers modulo `p` define a field, denoted `Fp`.
> If the modulus is not prime, the set of integers modulo n define a ring.

  
A finite field `Fp`​ is the set of integers 0,1,...,p−10,1,...,p−1, and under both addition and multiplication there are inverse elements `b+b+`​ and `b∗b∗`​ for every element `a` in the set, such that `a+b+=0` and `a⋅b∗=1`.

> Note that the identity element for addition and multiplication is different! This is because the identity when acted with the operator should do nothing: **a+0=a** and **a⋅1 = a**

Lets say we pick p=17. Calculate 317 mod  17. Now do the same but with 517mod  17.

What would you expect to get for 716 mod  17? Try calculating that.

This interesting fact is known as Fermat's little theorem. We'll be needing this (and its generalisations) when we look at RSA cryptography.
Now take the prime p=65537. Calculate 273246787654^65536 mod  65537.

---


## SOME RESEARCH ON OWN: 
### SO WHAT'S FINITE FIELD?? 
- **Finite field** or **Galois field** they both give the same meaning.
- The most common example of finite field are: the **intergers mod** p where p is a **prime number**.
- The order of finite field is its number: which is either a **prime number** or a **prime power**.
- For every prime number p and positive integer k there are fields of order p^k


## Fermat's Little Theorem

If $p$ is a prime number, then for any integer $a$, the number $a^p - a$ is an integer multiple of $p$.

This is expressed as:

$$a^{p} \equiv a \pmod{p}$$

If $a$ is not divisible by $p$, this is equivalent to:

$$a^{p-1} \equiv 1 \pmod{p}$$


## ANALYSIS FOR THIS CHALLENGE: 
- I saw that the number: `273246787654` is not divisible by `65537` so the result is equivalent to `1` not to the value of a.