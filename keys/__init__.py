class RSAPrivateKey:
    def __init__(self, n, d):
        self.n = n  # модуль
        self.d = d  # закрытая экспонента
    def __str__(self):
        return f"Private Key with N = {self.n}, D = {self.d}\n"
class RSAPublicKey:
    def __init__(self, n, e):
        self.n = n  # модуль
        self.e = e  # открытая экспонента
    def __str__(self):
        return f"Public Key with N = {self.n}, E = {self.e}\n"