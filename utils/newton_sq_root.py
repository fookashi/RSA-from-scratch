def isqrt(number: int):
    a, b = divmod(number.bit_length(), 2)
    x = 2 ** (a + b)
    for _ in iter(int, 1):
        root = (x + number // x) // 2
        if root >= x:
            return root
        x = root

