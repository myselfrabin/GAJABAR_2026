import base64

def hex_to_b64(hex_string: str) -> bytes:
    """convert hex string to base64 and return as bytes"""
    raw = bytes.fromhex(hex_string
                        )
    return base64.b64encode(raw) # raw bytes -> base64 bytes

if __name__ == "__main__":
    hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

    expected_base64 = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    result = hex_to_b64(hex_string)


    print(result.decode())

    assert hex_to_b64(hex_string) == expected_base64
    print('Challenge 1 passed')



