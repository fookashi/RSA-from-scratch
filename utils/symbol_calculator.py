from rsa.utils.gcd import extended_gcd

class SymbolCalculator:
    def legendre(self, a, p):
        if p <= 0 or (p % 2 == 0 and p != 2):
            raise ValueError("p должно быть простым числом или 2")

        a = a % p
        if a < 0:
            a += p  # Приводим a к положительному значению в диапазоне [0, p)
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
        if a < 0:
            if (n-1)//2 % 2 == 0:
                return self.jacobi(-a, n)
            else:
                return -self.jacobi(-a, n)
        if a % 2 == 0:
            if (n**2 - 1)//8 % 2 == 0:
                return self.jacobi(a // 2, n)
            else:
                return -self.jacobi(a // 2, n)
        g = extended_gcd(a,n)[0]
        if g == a:
            return 0
        elif g != 1:
            return self.jacobi(g, n) * self.jacobi(a // g, n)
        elif (a - 1) * ((n - 1) // 4) % 2 == 0:
            return self.jacobi(n, a)
        else:
            return -self.jacobi(n, a)