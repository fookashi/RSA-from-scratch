def isqrt(number: int):
    a, b = divmod(number.bit_length(), 2)
    x = 2 ** (a + b)
    root = 0
    for _ in iter(int, 1):
        root = (x + (number // x)) // 2
        if root >= x:
            break
        x = root

    return root