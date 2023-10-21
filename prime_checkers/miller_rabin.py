from rsa.interfaces import IPrimalityTester
from random import randint
from math import ceil, log, log2

class MillerRabinTester(IPrimalityTester):
    def __init__(self):
        self.r = None
        self.d = None

    def _single_iteration(self, n: int) -> bool:
        # Вычислить параметры n-1 = 2^r * d, где d - нечётное


        a = randint(2, n - 2)
        x = pow(a, self.d, n)

        if x == 1 or x == n - 1:
            return True

        for _ in range(self.r - 1):
            x = (x * x) % n
            if x == n - 1:
                return True

        return False

    def is_prime(self, n: int, p: float) -> bool:
        if n < 2 or n % 2 == 0:
            return False
        error_p = 1 - p
        first_k = ceil(log2(n))
        second_k = ceil(log(error_p, 0.5) / 2)
        k = first_k if first_k > second_k else second_k

        self.r, self.d = 0, n - 1
        while self.d % 2 == 0:
            self.r += 1
            self.d //= 2

        for _ in range(k):
            if not self._single_iteration(n):
                return False
        return True
