## XOR 
## 0    0   0
## 1    0   1
## 0    1   1
## 1    0   0

## XOR GIVES US 1 when two of the input are complete different, it gives 0 if two of the inputs are 
## same.



## i can convert the string into binary number using the base2 and then performing the XOR there cause
## we can't use ^ operator in strings to perform 




def hex_to_bytes(hex_str)-> bytes:
    """hex text --> raw.bytes"""

    return bytes.fromhex(hex_str)


def fixed_xor(a:bytes,b:bytes)-> bytes:
    """XOR two equal-length byte strings,byte by byte"""
    if len(a) != len(b):
        raise ValueError("buffers must be the same length")
    return bytes(x ^ y for x,y in zip(a,b))




if __name__ == "__main__":
    hex_a = '1c0111001f010100061a024b53535009181c'
    hex_b = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'

    results = fixed_xor(hex_to_bytes(hex_a),hex_to_bytes(hex_b))

    print(results.hex())
    print(results)

    assert results.hex() == expected
    print('Challenge 2 passed')
