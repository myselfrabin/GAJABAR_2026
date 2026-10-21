def extended_gcd_recursive(a, b):
    """
    Returns a tuple (gcd, x, y) using structural recursion.
    """
    if b == 0:
        return a, 1, 0
    
    gcd, x1, y1 = extended_gcd_recursive(b, a % b)
    
    # Update coefficients using the results of the recursive call
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

# Example Usage
a, b = 26513, 32321
gcd, x, y = extended_gcd_recursive(a, b)
print(f"GCD({a}, {b}) = {gcd}")
print(f"Coefficients: x = {x}, y = {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {a * x + b * y}")

