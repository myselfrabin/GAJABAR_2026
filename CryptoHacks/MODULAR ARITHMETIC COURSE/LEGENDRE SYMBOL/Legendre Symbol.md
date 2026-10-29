
---
In Quadratic Residues we learnt what it means to take the square root modulo an integer. We also saw that taking a root isn't always possible.

  
In the previous case when **p=29**, even the simplest method of calculating the square root was fast enough, but as pp gets larger, this method becomes wildly unreasonable.  
  
Lucky for us, we have a way to check whether an integer is a quadratic residue with a single calculation thanks to Legendre. In the following, we will assume we are working modulo a prime pp.  
  
Before looking at Legendre's symbol, let's take a brief detour to see an interesting property of quadratic (non-)residues.

```text
Quadratic Residue * Quadratic Residue = Quadratic Residue  
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue  
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue
```

> Want an easy way to remember this? Replace "Quadratic Residue" with +1 and "Quadratic Non-residue" with −1, all three results are the same!

So what's the trick? The [Legendre Symbol](https://en.wikipedia.org/wiki/Legendre_symbol) gives an efficient way to determine whether an integer is a quadratic residue modulo an odd prime p.

Legendre's Symbol: 

$$
\left(\frac{a}{p}\right) \equiv a^{\frac{p-1}{2}} \pmod p obeys
$$


> [!info] Legendre Symbol Definition
> The Legendre symbol is defined as:
> $$\left(\frac{a}{p}\right) = \begin{cases} 1 & \text{if } a \text{ is a QR } \pmod p \text{ and } a \not\equiv 0 \pmod p \\ -1 & \text{if } a \text{ is a QNR } \pmod p \\ 0 & \text{if } a \equiv 0 \pmod p \end{cases}$$

Which means given any integer aa, calculating a(p−1)/2mod  p is enough to determine if a is a quadratic residue.

Now for the flag. Given the following 1024 bit prime and 10 integers, find the quadratic residue and then calculate its square root; the square root is your flag. Of the two possible roots, submit the larger one as your answer.

> So Legendre's symbol tells us which integer is a quadratic residue, but how do we find the square root?! The prime supplied obeys p=3mod  4, which allows us easily compute the square root. The answer is online, but you can figure it out yourself if you think about Fermat's little theorem.

[OutputFiles.txt](https://cryptohack.org/static/challenges/output_479698cde19aaa05d9e9dfca460f5443.txt)

---


## SOME RESEARCH: 

- So what actually is **Legendre Symbol**??
![](Attachments/Pasted%20image%2020261029160148.png)



- Legendre symbol is the useful notation for the **quadratic residue**.
- Legendre symbol of a with respect to p defined as 1 if a is quadratic residue mod p.
- Legendre symbol of a with respect to p defined as -1 if a is non-quadratic residue mod p.
- We put number on top (a/p) and modulus on buttom, this looks like fraction but it's not a fraction.


## LET'S SEE A EXAMPLE OF QUADRATIC RESIDUE OF MOD 5:

1 ^2 = 1    ---> (1/5) = 1 (if 1 is the quardractic residue of mod 5)
2 ^2= 4   -->  (4/5) = 1 (if 4 is the quadratic residue of mod 5)
3^2=9 = 4 (MOD 5)
4^2= 16 = 1 (MOD 5)
- Here 2 and 3 are quadratic non residue so
	- (2/5) = -1 
	- (3/5) = -1 