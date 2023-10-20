from utils.gcd import extended_gcd

class SymbolCalculator:
    def _is_quad_residue(self,a, p):
        for x in range(1,p):
            if pow(x,2,p) == a % p:
                return True
        return False
    def legendre(self, a, p):
        if p < 2:
            raise ValueError('p must not be < 2')
        if (a == 0) or (a == 1):
            return a
        if a % 2 == 0:
            r = self.legendre(a // 2, p)
            if p * p - 1 & 8 != 0:
                r *= -1
        else:
            r = self.legendre(p % a, a)
            if (a - 1) * (p - 1) & 4 != 0:
                r *= -1
        return r


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