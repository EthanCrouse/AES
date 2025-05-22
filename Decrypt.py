from InvShiftRows import InvShiftRows
from SubByte import InvSubBytes
from AddRoundKey import AddRoundKey
from InvMixColumns import InvMixColumns
from KeyExpansion import KeyExpansion


def format(a):
    return ''.join(f"{byte:02x}" for byte in a)

def Decrypt_Core(ciphertext, key, nr):
    state = list(ciphertext)
    state = AddRoundKey(state, key[16*nr:16*(nr+1)])

    for i in range(nr - 1, 0, -1):
        state = InvShiftRows(state)
        state = InvSubBytes(state)
        state = AddRoundKey(state, key[16 * i:16 * (i + 1)])
        state = InvMixColumns(state)

    state = InvShiftRows(state)
    state = InvSubBytes(state)
    state = AddRoundKey(state, key[:16])
    return state

def Decrypt_CBC(ciphertext, key):
    key_length = len(key)

    if key_length == 176: nr = 10
    elif key_length == 216: nr = 12
    elif key_length == 256: nr = 14

    plaintext = []

    for i in range(0, len(ciphertext), 16):
        current_block = ciphertext[i:i + 16]
        decrypted_block = Decrypt_Core(current_block, key, nr)
        if i != 0:
            decrypted_block = AddRoundKey(decrypted_block, ciphertext[i - 16:i])
        plaintext.extend(decrypted_block)

    return format(plaintext)

def Decrypt_ECB(ciphertext, key):
    key_length = len(key)

    if key_length == 176: nr = 10
    elif key_length == 216: nr = 12
    elif key_length == 256: nr = 14

    plaintext = []

    for i in range(0, len(ciphertext), 16):
        current_block = ciphertext[i:i + 16]
        decrypted_block = Decrypt_Core(current_block, key, nr)
        plaintext.extend(decrypted_block)

    return format(plaintext)

def Decrypt(ciphertext, key, mode):
    ciphertext = bytes.fromhex(ciphertext)
    key = KeyExpansion(key)
    if mode.__eq__("CBC"): return Decrypt_CBC(ciphertext, key)
    if mode.__eq__("ECB"): return Decrypt_ECB(ciphertext, key)