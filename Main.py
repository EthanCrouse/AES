from Encrypt import Encrypt
from Decrypt import Decrypt

if __name__ == "__main__":
    cry_input = input("Enter '1' for Encryption and '0' for Decrpytion: ")
    mode_input = input("Enter mode 'ECB' or 'CBC': ")
    text_input = input("Enter text: ")
    key_input = input("Enter key: ")

    
    str = ''
    if cry_input.__eq__('0'):
        str = Decrypt(text_input, key_input, mode_input)
    elif cry_input.__eq__('1'):
        str = Encrypt(text_input, key_input, mode_input)
    else:
        print(f"-"*100)
        print("Fail: Incorrect parameter given for encrpytion or decryption")

    print(f"-"*100)
    print(f"Output text: {str}")
