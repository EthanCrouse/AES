from ByteManupulation import multiply, xtimes

"""
MixColumns Function
This function takes a array of 16 bytes and applies the MixColumns transformation
[2, 3, 1, 1]
[1, 2, 3, 1]
[1, 1, 2, 3]
[3, 1, 1, 2]
"""

def format(a):
    return f"{a:02x}"

def MixColumns(a):
    temp = [0] * 16
    temp[0] = multiply(a[0], 2) ^ multiply(a[1], 3) ^ a[2] ^ a[3]
    temp[1] = a[0] ^ multiply(a[1], 2) ^ multiply(a[2], 3) ^ a[3]
    temp[2] = a[0] ^ a[1] ^ multiply(a[2], 2) ^ multiply(a[3], 3)
    temp[3] = multiply(a[0], 3) ^ a[1] ^ a[2] ^ multiply(a[3], 2)

    temp[4] = multiply(a[4], 2) ^ multiply(a[5], 3) ^ a[6] ^ a[7]
    temp[5] = a[4] ^ multiply(a[5], 2) ^ multiply(a[6], 3) ^ a[7]
    temp[6] = a[4] ^ a[5] ^ multiply(a[6], 2) ^ multiply(a[7], 3)
    temp[7] = multiply(a[4], 3) ^ a[5] ^ a[6] ^ multiply(a[7], 2)

    temp[8] = multiply(a[8], 2) ^ multiply(a[9], 3) ^ a[10] ^ a[11]
    temp[9] = a[8] ^ multiply(a[9], 2) ^ multiply(a[10], 3) ^ a[11]
    temp[10] = a[8] ^ a[9] ^ multiply(a[10], 2) ^ multiply(a[11], 3)
    temp[11] = multiply(a[8], 3) ^ a[9] ^ a[10] ^ multiply(a[11], 2)

    temp[12] = multiply(a[12], 2) ^ multiply(a[13], 3) ^ a[14] ^ a[15]
    temp[13] = a[12] ^ multiply(a[13], 2) ^ multiply(a[14], 3) ^ a[15]
    temp[14] = a[12] ^ a[13] ^ multiply(a[14], 2) ^ multiply(a[15], 3)
    temp[15] = multiply(a[12], 3) ^ a[13] ^ a[14] ^ multiply(a[15], 2)

    return temp

def transpose_arr(a):
    """
    tranpose the array a acting like it is a 4x4 matrix
    in the following way
    [0, 1, 2, 3]
    [4, 5, 6, 7]
    [8, 9, 10, 11]
    [12, 13, 14, 15]
    """
    temp = [0] * 16
    for i in range(4):
        for j in range(4):
            temp[i*4+j] = a[j*4+i]
    return temp
    


def print_matrix(a):
    """Prints a 16-byte list as a 4×4 hex matrix."""
    for i in range(4):
        row = a[i*4:(i+1)*4]
        print(' '.join(f"{b:02x}" for b in row))

if __name__ == "__main__":
    
    a = [
        0xdb, 0xf2, 0x01, 0xc6,
        0x13, 0x0a, 0x01, 0xc6,
        0x53, 0x22, 0x01, 0xc6,
        0x45, 0x5c, 0x01, 0xc6
    ]
    print("Original:")
    print_matrix(a)
    print("After MixColumns:")
    print_matrix(MixColumns(a))