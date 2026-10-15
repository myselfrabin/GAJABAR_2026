encodedString = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

def decodeString(encodedString):
    """change string to hex first"""

    hexEncoded = bytes.fromhex(encodedString)

    return hexEncoded


if __name__=="__main__":
    print('Finding the flag............')

    result = decodeString(encodedString)

    print(result.decode())

