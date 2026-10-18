## we'll be using the recursive method for the GCD



def compute_gcd_recursive(a,b):
    if b == 0:
        return a 
    return compute_gcd_recursive(b,a%b)

print(compute_gcd_recursive(66528,52920))
