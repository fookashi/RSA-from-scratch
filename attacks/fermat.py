from rsa.utils.mod_inverser import ModInverser
from rsa.utils.newtons_root import isqrt
from rsa.interfaces import IAttacker
from rsa.keys import RSAPublicKey


class FermatAttacker(IAttacker):

    def attack(self, public_key: RSAPublicKey):
        e, n = public_key.e, public_key.n
        a = isqrt(n)
        temp = a**2 - n
        b = isqrt(temp)
        while b**2 != temp:
            a = a + 1
            temp = a * a - n
            b = isqrt(temp)
        p = a + b
        q = a - b
        phi_n = (p - 1) * (q - 1)
        d = ModInverser().calculate_mod_inverse(e, phi_n)
        return d