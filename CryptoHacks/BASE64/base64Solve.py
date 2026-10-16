import base64
from urllib.parse import unquote


hexString = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

def base64f(hexString):
    """firstly we will decode that string in bytes"""
    byte_data = bytes.fromhex(hexString)
    
    return base64.b64encode(byte_data).decode('utf-8')
if __name__=="__main__":
    print('Finding the flag................')

    result = base64f(hexString)
    
    print(f"The flag is:  {result}")
