from utils.mod_inverser import ModInverser
from utils.newton_sq_root import isqrt
from interfaces import IAttacker

class FermatAttacker(IAttacker):
    def attack(self, n: int, e: int):
        a = isqrt(n)
        temp = a**2 - n
        b = isqrt(temp)
        while b**2 != temp:
            print(f'Trying: a={a} temp={temp} b={b}')
            a = a + 1
            temp = a * a - n
            b = isqrt(temp)
        p = a + b
        q = a - b
        phi_n = (p - 1) * (q - 1)
        d = ModInverser().calculate_mod_inverse(e, phi_n)
        return d