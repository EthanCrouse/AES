from Inverse import get_inverse

#######################################################################
####### Byte Manipulation                                       #######
#######################################################################

# Add In Mod 2 Using XOR
def add(a, b):
    return [x ^ y for x, y in zip(a, b)]

# Xtimes
def xtimes(a):
    a &= 0xFF
    result = a << 1
    if (result & 0x100) != 0:
        result ^= 0x11B
    return result & 0xFF

# Multiply
def multiply(a, b):
    a &= 0xFF
    b &= 0xFF
    result = 0
    for _ in range(8):
        if (b & 1) != 0:
            result ^= a
        a = xtimes(a)
        b >>= 1
    return result & 0xFF

# Inverse
def inverse(a):
    return get_inverse(a)