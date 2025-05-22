from ByteManupulation import multiply, xtimes

"""
MixColumns Function
This function takes a array of 16 bytes and applies the MixColumns transformation
[2, 3, 1, 1]
[1, 2, 3, 1]
[1, 1, 2, 3]
[3, 1, 1, 2]

[0x0E, 0x0B, 0x0D, 0x09]
[0x09, 0x0E, 0x0B, 0x0D]
[0x0D, 0x09, 0x0E, 0x0B]
[0x0B, 0x0D, 0x09, 0x0E]
"""

def format(a):
    return f"{a:02x}"

def InvMixColumns(a):
    x = 0x0E
    y = 0x0B
    z = 0x0D
    k = 0x09

    temp = [0] * 16
    temp[0] = multiply(a[0], x) ^ multiply(a[1], y) ^ multiply(a[2], z) ^ multiply(a[3], k)
    temp[1] = multiply(a[0], k) ^ multiply(a[1], x) ^ multiply(a[2], y) ^ multiply(a[3], z)
    temp[2] = multiply(a[0], z) ^ multiply(a[1], k) ^ multiply(a[2], x) ^ multiply(a[3], y)
    temp[3] = multiply(a[0], y) ^ multiply(a[1], z) ^ multiply(a[2], k) ^ multiply(a[3], x)

    temp[4] = multiply(a[4], x) ^ multiply(a[5], y) ^ multiply(a[6], z) ^ multiply(a[7], k)
    temp[5] = multiply(a[4], k) ^ multiply(a[5], x) ^ multiply(a[6], y) ^ multiply(a[7], z)
    temp[6] = multiply(a[4], z) ^ multiply(a[5], k) ^ multiply(a[6], x) ^ multiply(a[7], y)
    temp[7] = multiply(a[4], y) ^ multiply(a[5], z) ^ multiply(a[6], k) ^ multiply(a[7], x)

    temp[8] = multiply(a[8], x) ^ multiply(a[9], y) ^ multiply(a[10], z) ^ multiply(a[11], k)
    temp[9] = multiply(a[8], k) ^ multiply(a[9], x) ^ multiply(a[10], y) ^ multiply(a[11], z)
    temp[10] = multiply(a[8], z) ^ multiply(a[9], k) ^ multiply(a[10], x) ^ multiply(a[11], y)
    temp[11] = multiply(a[8], y) ^ multiply(a[9], z) ^ multiply(a[10], k) ^ multiply(a[11], x)

    temp[12] = multiply(a[12], x) ^ multiply(a[13], y) ^ multiply(a[14], z) ^ multiply(a[15], k)
    temp[13] = multiply(a[12], k) ^ multiply(a[13], x) ^ multiply(a[14], y) ^ multiply(a[15], z)
    temp[14] = multiply(a[12], z) ^ multiply(a[13], k) ^ multiply(a[14], x) ^ multiply(a[15], y)
    temp[15] = multiply(a[12], y) ^ multiply(a[13], z) ^ multiply(a[14], k) ^ multiply(a[15], x)

    return temp

    


