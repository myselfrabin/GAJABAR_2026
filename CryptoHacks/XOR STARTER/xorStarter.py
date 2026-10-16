string = 'label'

def xor(string: str) -> str:
    keyInt = 13
    flag = "".join(chr(ord(char) ^ keyInt) for char in string)
    return flag


if __name__ == "__main__":
    result = xor(string)  # replace with your actual string
    print("Getting the flag...............")
    print(result)
