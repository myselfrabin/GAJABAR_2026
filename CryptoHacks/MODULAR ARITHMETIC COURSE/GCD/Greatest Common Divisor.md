
---
The Greatest Common Divisor (GCD), sometimes known as the highest common factor, is the largest number which divides two positive integers (a,b)(a,b).  
  
For a=12,b=8a=12,b=8 we can calculate the divisors of aa: {1,2,3,4,6,12}{1,2,3,4,6,12} and the divisors of bb: {1,2,4,8}{1,2,4,8}. Comparing these two, we see that gcd⁡(a,b)=4gcd(a,b)=4.  
  
Now imagine we take a=11,b=17a=11,b=17. Both aa and bb are prime numbers. As a prime number has only itself and 11 as divisors, gcd⁡(a,b)=1gcd(a,b)=1.  
  
We say that for any two integers a,ba,b, if gcd⁡(a,b)=1gcd(a,b)=1 then aa and bb are coprime integers.  
  
If a and b are prime, they are also coprime. If a is prime and  b < a , then a and b are the coprime.

> Think about the case for a prime and b > a , why this are not necessiarly coprime?? 

There are many tools to calculate the GCD of two integers, but for this task we recommend looking up [Euclid's Algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm).

Try coding it up; it's only a couple of lines. Use a = 12, b = 8 to test it

Now calculate `gcd(a,b) for a = 66528, b = 52920` and enter it below.

---

## WHAT'S EUCLIDEAN ALGORITHM? 
- The Euclidean algorithm is an efficent method for computing the `greatest common divisor(GCD)` of two intergers, the largest number that divides them both without the remainder.
- It's based on the principle that `the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number.` Example: 21 is GCD of 252 and 105 (as 252= 21 * 12 and 105 = 21 * 5), and the same number 21 is also the GCD of 105 and 252-105 = 147.
- If gcd(a,b) = 1 then a and b are said to be `coprime( or relatively prime)`. This property does not imply that a and b ar e themselves prime numbers. For example: 6 and 35 factors as 6 = 2 * 3  and 35 = 5 * 7 so they are not prime, but their prime factors are different, so 6 and 35 are `coprime` , with no common factors other then 1. 

## ANALYSIS: 
- So using the recursive algorithm in python I solved this challenge

![](Attachments/Pasted%20image%2020261018172557.png)






