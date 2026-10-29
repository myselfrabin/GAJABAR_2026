'''
we have given a file with lists of integers
and a prime number too there
let's first work with that file and do our work

'''

import ast


def legendre_symbol(a, p):
    """Calculate the Legendre symbol (a/p)."""
    a %= p

    if a == 0:
        return 0

    result = pow(a, (p - 1) // 2, p)

    if result == p - 1:
        return -1

    return result


if __name__ == "__main__":

    # Read the challenge file
    with open(
        "./output_479698cde19aaa05d9e9dfca460f5443.txt",
        "r"
    ) as file:
        content = file.read()

    # Extract the integers and prime
    ints = None
    primeVal = None

    for line in content.splitlines():
        line = line.strip()

        if line.startswith("ints"):
            val_str = line.split("=", 1)[1].strip()
            ints = ast.literal_eval(val_str)

        elif line.startswith("p"):
            val_str = line.split("=", 1)[1].strip()
            primeVal = ast.literal_eval(val_str)

    # Check that both values were loaded
    if ints is None or primeVal is None:
        raise ValueError("Could not find ints or p in the file")

    print(f"Prime loaded: {primeVal}")
    print(f"Number of integers: {len(ints)}")

    # The challenge requires p = 3 mod 4
    if primeVal % 4 != 3:
        raise ValueError("The prime does not satisfy p % 4 == 3")

    # Find the quadratic residue and its square root
    found = False

    for a in ints:
        symbol = legendre_symbol(a, primeVal)

        print(f"Legendre symbol of {a}: {symbol}")

        if symbol == 1:
            print("\nQuadratic residue found:", a)

            # Calculate one square root modulo p
            root1 = pow(a, (primeVal + 1) // 4, primeVal)

            # Calculate the other square root modulo p
            root2 = (-root1) % primeVal

            # Select the larger root
            flag = max(root1, root2)

            # Verify the result
            if pow(flag, 2, primeVal) == a % primeVal:
                print("\nRoot 1:", root1)
                print("Root 2:", root2)
                print("\nFlag:", flag)
                found = True
                break

            else:
                print("Square root verification failed!")

    if not found:
        print("\nNo quadratic residue with symbol 1 was found.")
