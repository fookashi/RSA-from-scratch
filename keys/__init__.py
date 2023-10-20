class RSAPrivateKey:
    def __init__(self, n, d):
        self.n = n  # модуль
        self.d = d  # закрытая экспонента


class RSAPublicKey:
    def __init__(self, n, e):
        self.n = n  # модуль
        self.e = e  # открытая экспонента
