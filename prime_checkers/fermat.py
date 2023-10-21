import math

from rsa.interfaces import IPrimalityTester
from random import randint
from math import log, ceil

class FermatTester(IPrimalityTester):
    def _single_iteration(self, n: int) -> bool:
        a = randint(2, n - 2)
        return pow(a, n - 1, n) == 1

    def is_prime(self, n: int, p: float) -> bool:
        if n < 2 or n % 2 == 0:
            return False
        error_p = 1 - p
        k = ceil(math.log(error_p, 0.5))
        for _ in range(k):
            if not self._single_iteration(n):
                return False
        return True
