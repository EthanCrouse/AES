from SubByte import get_sub
from ByteManupulation import add
from ByteManupulation import xtimes

#######################################################################
####### Key Expansion Helper Functions                          #######
#######################################################################

# Rotates 4 Bytes To Left By 1
def RotateLeft(byte1, byte2, byte3, byte4):
    return [byte2, byte3, byte4, byte1]

# Gets Subsitute From subbyte.py
def SubByte(a):
    return get_sub(a)

def SubBytes(a):
    return get_sub(a[0]), get_sub(a[1]), get_sub(a[2]), get_sub(a[3])

def AddRoundConstant(a, b, c, d, round):
    rcon = 0x01
    for _ in range(round - 1):
        rcon = xtimes(rcon)
    
    return a ^ rcon, b, c, d

# Key Expansion Core Routine
def KeyExpansionCore(byte1, byte2, byte3, byte4, round):
    arr = RotateLeft(byte1, byte2, byte3, byte4)
    byte1 = SubByte(arr[0])
    byte2 = SubByte(arr[1])
    byte3 = SubByte(arr[2])
    byte4 = SubByte(arr[3])
    arr[0], arr[1], arr[2], arr[3] = AddRoundConstant(byte1, byte2, byte3, byte4, round)
    return (arr[0], arr[1], arr[2], arr[3])

#######################################################################
####### Key Expansion 128, 192, and 256                         #######
#######################################################################

# 128
def KeyExpansion128(initialKey):
    initialKey = formatInitialKey(initialKey)
    round = 1
    ExpansionKey = initialKey
    while len(ExpansionKey) < 176:
        for i in range(4):
            temp1 = ExpansionKey[-4:]
            if (i==0):
                temp1 = KeyExpansionCore(temp1[0], temp1[1], temp1[2], temp1[3], round)
            temp2 = ExpansionKey[-16:]
            temp2 = temp2[:4]
            ExpansionKey += add(list(temp1), list(temp2))
        round+=1
    #ExpansionKey = formatKey(ExpansionKey)
    return ExpansionKey

# 192
def KeyExpansion192(initialKey):
    initialKey = formatInitialKey(initialKey)
    round = 1
    ExpansionKey = initialKey
    while len(ExpansionKey) < 208:
        for i in range(6):
            temp1 = ExpansionKey[-4:]
            if (i==0):
                temp1 = KeyExpansionCore(temp1[0], temp1[1], temp1[2], temp1[3], round)
            temp2 = ExpansionKey[-24:]
            temp2 = temp2[:4]
            ExpansionKey += add(temp1, temp2)
        round+=1
    #ExpansionKey = formatKey(ExpansionKey)
    return ExpansionKey

# 256
def KeyExpansion256(initialKey):
    initialKey = formatInitialKey(initialKey)
    round = 1
    ExpansionKey = initialKey
    while (len(ExpansionKey) < 240):
        for i in range(8):
            temp1 = ExpansionKey[-4:]
            if (i==0):
                temp1 = KeyExpansionCore(temp1[0], temp1[1], temp1[2], temp1[3], round)
            if (i==4):
                temp1 = SubBytes(temp1)
            temp2 = ExpansionKey[-32:]
            temp2 = temp2[:4]
            ExpansionKey += add(temp1, temp2)
        round+=1
    #ExpansionKey = formatKey(ExpansionKey)
    return ExpansionKey

def KeyExpansion(key):
    N = len(key)/2
    if (N == 16): return KeyExpansion128(key)
    if (N == 24): return KeyExpansion192(key)
    if (N == 32): return KeyExpansion256(key)

    print(f"Incorrect Key Length...Length of key is {N}")
    return 0

#######################################################################
####### Formatting                                              #######
#######################################################################

# Format Final Key To String
def formatKey(key):
    formatedKey = ""
    for i in key:
        formatedKey += (f"{i:02x}")
    return formatedKey

# Format Initial String Key to Hex
def formatInitialKey(key):
    return [int(key[i:i+2], 16) for i in range(0, len(key), 2)]

#######################################################################
####### Main                                                    #######
#######################################################################
if __name__ == "__main__":
    initialKey128 = "3A7F91C4E2059B8D1F3B6A27D8C0F492"
    initialKey192 = "3A7F91C4E2059B8D1F3B6A27D8C0F4923A7F91C4E2059B8D"
    initialKey256 = "3A7F91C4E2059B8D1F3B6A27D8C0F4923A7F91C4E2059B8D1F3B6A27D8C0F492"
    ExpansionKey128 = KeyExpansion128(initialKey128)
    ExpansionKey192 = KeyExpansion192(initialKey192)
    ExpansionKey256 = KeyExpansion256(initialKey256)
    print(formatKey(ExpansionKey128))
    print(f"-"*100)
    print(formatKey(ExpansionKey192))
    print(f"-"*100)
    print(formatKey(ExpansionKey256))

