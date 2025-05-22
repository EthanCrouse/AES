def AddRoundKey(a: list[int], b: list[int]) -> list[int]:
    """
    XORs the state with the round key in-place.
    """
    state = [0] * 16
    for i in range(16):
        state[i] = a[i] ^ b[i]
    return state