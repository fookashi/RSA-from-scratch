from rsa.utils.gcd import extended_gcd

class SymbolCalculator:
    def legendre(self, a, p):
        if p <= 0 or (p % 2 == 0 and p != 2):
            raise ValueError("p должно быть простым числом или 2")

        a = a % p
        if a < 0:
            a += p  # a to [0, p)
        if a == 0:
            return 0
        if a == 1:
            return 1
        if a % 2 == 0:
            return self.legendre(a // 2, p) * (-1) ** ((p ** 2 - 1) // 8)
        else:
            return self.legendre(p % a, a) * (-1) ** ((a - 1) * (p - 1) // 4)

    def jacobi(self, a, n):
        if a >= n:
            a = a % n
        if a == 0:
            return 0
        if a == 1:
            return 1
        if a == 2:
            n8 = n % 8
            if n8 == 3 or n8 == 5:
                return -1
            else:
                return 1
        if a % 2 == 0:
            return self.jacobi(2, n) * self.jacobi(a // 2, n)
        if a % 4 == 3 and n % 4 == 3:
            return -self.jacobi(n, a)
        else:
            return self.jacobi(n, a)