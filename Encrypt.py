from SubByte          import SubBytes
from KeyExpansion     import KeyExpansion
from ShiftRows        import ShiftRows
from MixColumns       import MixColumns
from AddRoundKey      import AddRoundKey


#####################################################################################
####### Helper Functions                                                      #######
#####################################################################################

def format(a):
    formated = ""
    for i in a:
        formated += (f"{i:02x}")
    return formated


##################################################################################
############ ECB Encryption                                           ############                        
##################################################################################
def EncryptCore128_ECB(text, key):
    """
    Encrypts one 16-byte block (hex) using pre-computed round_keys.
    """
    state = [0] * 16
    for i in range(16):
        state[i] = text[i]
        
    state = AddRoundKey(state, key[0:16])

    for i in range(9):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[16 * (i + 1): 16 * (i + 2)])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[160:176])

    state = format(state)
    return state

def EncryptCore192_ECB(text, key):
    state = [0]*16
    for i in range(16):
        state[i] = text[i]

    # initial AddRoundKey
    state = AddRoundKey(state, key[0:16])
    # 11 full rounds
    for i in range(11):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[16 * (i + 1): 16 * (i + 2)])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[16*12 : 16*13])
    
    state = format(state)
    return state

def EncryptCore256_ECB(text, key):
    state = [0]*16
    for i in range(16):
        state[i] = text[i]

    # initial AddRoundKey
    state = AddRoundKey(state, key[0:16])
    # 13 full rounds
    for i in range(13):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[16 * (i + 1): 16 * (i + 2)])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[16*14 : 16*15])
    
    state = format(state)
    return state

def Encrypt_ECB(message_bytes, key):
    key = KeyExpansion(key)
    key_length = len(key)
    ciphertext = ""

    print(key_length)

    for i in range(0, len(message_bytes), 16):
        block = message_bytes[i:i + 16]
        if key_length == 176: ciphertext += EncryptCore128_ECB(block, key)
        elif key_length == 216: ciphertext += EncryptCore192_ECB(block, key)
        elif key_length == 256: ciphertext += EncryptCore256_ECB(block, key)
        

    return ciphertext


##################################################################################
############ CBC Encryption                                           ############                        
##################################################################################

def EncryptCore128_CBC(text, key, prev):
    """
    Encrypts one 16-byte block (hex) using pre-computed round_keys.
    """
    state = [0] * 16
    for i in range(16):
        state[i] = text[i]
    
    if prev == 0x11b: state = AddRoundKey(state, key[0:16])
    else:
        state = AddRoundKey(state, key[0:16])
        state = AddRoundKey(state, prev)
        

    for i in range(9):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[16 * (i + 1): 16 * (i + 2)])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[160:176])

    return state

def EncryptCore192_CBC(text, key, prev):
    state = [0]*16
    for i in range(16):
        state[i] = text[i]

    # initial AddRoundKey
    if prev == 0x11b: state = AddRoundKey(state, key[0:16])
    else:
        state = AddRoundKey(state, key[0:16])
        state = AddRoundKey(state, prev)
    # 11 full rounds
    for i in range(11):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[16 * (i + 1): 16 * (i + 2)])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[16*12 : 16*13])
    
    return state

def EncryptCore256_CBC(text, key, prev):
    state = [0]*16
    for i in range(16):
        state[i] = text[i]

    # initial AddRoundKey
    if prev == 0x11b: state = AddRoundKey(state, key[0:16])
    else:
        state = AddRoundKey(state, key[0:16])
        state = AddRoundKey(state, prev)
    # 13 full rounds
    for i in range(13):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[16 * (i + 1): 16 * (i + 2)])

    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[16*14 : 16*15])
    
    return state

def Encrypt_CBC(message_bytes, key):
    key = KeyExpansion(key)
    key_length = len(key)
    ciphertext = ""


    prev_block = 0x11b
    for i in range(0, len(message_bytes), 16):
        block = message_bytes[i:i + 16]
        if key_length == 176: prev_block = EncryptCore128_CBC(block, key, prev_block)
        elif key_length == 216: prev_block = EncryptCore192_CBC(block, key, prev_block)
        elif key_length == 256: prev_block = EncryptCore256_CBC(block, key, prev_block)
        ciphertext += format(prev_block)
        

    return ciphertext


def Encrypt(text, key, mode):
    text = bytes.fromhex(text)
    if mode.__eq__("CBC"): return Encrypt_CBC(text, key)
    if mode.__eq__("ECB"): return Encrypt_ECB(text, key)

#####################################################################################
####### Main                                                                  #######
#####################################################################################

if __name__ == "__main__":

    plaintext_hex   = "a227bcee08e0b534de59cd2d8926f138a48902811ed6776ac60291ddf93375ce38de1016f29c45e95e4249d0b35cd8c0009ef90a6b075856b00498113e41a2a03129f6254b27e7b0977b57fb0f6bb958e7e6806a906e7a246e4d6e0a6dfd4452f9bd3855d1168ec02945c7ccf571d7a2faef813d03322a5de714bc65d7a2557a868b172f1436bd41c48450c2cc852ba3eed212e8b74017d24c288c7141b677de714f1741927aaf114c44b3979b2a4b359a2e936161cede0e9387c6dcf38b82f44400a4c51889f43e4a9caf08f1764cef"
    key             = "f839739fff1d95775ebcd6d16586ccacd4eadfcae84b1643df3cb7598d92e0d4"
    
    plaintext = bytes.fromhex(plaintext_hex)
    ciphertext = Encrypt_CBC(plaintext, key)

    print("Plaintext:", plaintext)
    print("Key:", key)
    print("Ciphertext:", ciphertext)
