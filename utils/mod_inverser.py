from rsa.interfaces import IModInverseCalculator
from rsa.utils.gcd import extended_gcd

class ModInverser(IModInverseCalculator):
    def calculate_mod_inverse(self, a, m):
        g, x, y = extended_gcd(a, m)
        if g != 1:
            raise ValueError("Inversed element not existing.")
        else:
            return x % m

