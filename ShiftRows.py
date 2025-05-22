
"""
ShiftRows function for AES encryption.
This function takes a 16-byte state array and performs the ShiftRows transformation,
"""
def ShiftRows(a):
    """
    [0, 1, 2, 3,  
    4, 5, 6, 7,
    8, 9, 10, 11
    12, 13, 14, 15]

    ---->

    [0, 1, 2, 3,
    5, 6, 7, 4,
    10, 11, 8, 9,
    15, 12, 13, 14]
    
    
    
    """
    temp = [0] * 16
    temp[0] = a[0]
    temp[1] = a[5]
    temp[2] = a[10]
    temp[3] = a[15]

    temp[4] = a[4]
    temp[5] = a[9]
    temp[6] = a[14]
    temp[7] = a[3]

    temp[8] = a[8]
    temp[9] = a[13]
    temp[10] = a[2]
    temp[11] = a[7]

    temp[12] = a[12]
    temp[13] = a[1]
    temp[14] = a[6]
    temp[15] = a[11]
    
    for i in range(16):
        a[i] = temp[i]
    return a


if __name__ == "__main__":
    """
    test
    """
    def matrix(a):
        for i in range(4):
            print(a[i*4:i*4+4])
            pass

    a = [0, 1, 2, 3,
         4, 5, 6, 7,
         8, 9, 10, 11,
         12, 13, 14, 15]
    matrix(a)
    print("ShiftRows")
    a = ShiftRows(a)
    matrix(a)
    
