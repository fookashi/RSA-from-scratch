from rsa.utils.newtons_root import isqrt
from rsa.interfaces import IAttacker
from rsa.keys import RSAPublicKey
from typing import Iterator, Iterable

class WienerAttacker(IAttacker):

    def _is_perfect_square(self, n: int) -> bool:
        sq_mod256 = (
        1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1,
        0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1,
        0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0)
        if sq_mod256[n & 0xff] == 0:
            return False

        mt = (
            (9, (1, 1, 0, 0, 1, 0, 0, 1, 0)),
            (5, (1, 1, 0, 0, 1)),
            (7, (1, 1, 1, 0, 1, 0, 0)),
            (13, (1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1)),
            (17, (1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1))
        )
        a = n % (9 * 5 * 7 * 13 * 17)
        if any(t[a % m] == 0 for m, t in mt):
            return False

        return isqrt(n) ** 2 == n
    def _rational_to_contfrac(self, x: int, y: int) -> Iterator[int]:
        while y:
            a = x // y
            yield a
            x, y = y, x - a * y

    def _contfrac_to_fractions(self, contfrac: Iterable[int]) -> Iterator[tuple[int, int]]:
        k0, d0 = 0, 1
        k1, d1 = 1, 0
        for q in contfrac:
            n = q * k1 + k0
            d = q * d1 + d0
            yield n, d
            k0, d0 = k1, d1
            k1, d1 = n, d

    def _convergents_from_contfrac(self, contfrac: Iterable[int]) -> Iterator[tuple[int, int]]:
        n_, d_ = 1, 0
        for i, (n, d) in enumerate(self._contfrac_to_fractions(contfrac)):
            if i % 2 == 0:
                yield n + n_, d + d_
            else:
                yield n, d
            n_, d_ = n, d

    def solve_quadratic(self, n, phi):

        a = 1
        b = -(n - phi + 1)
        c = n
        discriminant = b ** 2 - 4 * a * c

        if discriminant >= 0:
            p = (-b + isqrt(discriminant)) / (2 * a)
            q = (-b - isqrt(discriminant)) / (2 * a)
            return p, q

        return None

    def attack(self, public_key: RSAPublicKey):
        e, n = public_key.e, public_key.n
        f_ = self._rational_to_contfrac(e, n)
        for k, dg in self._contfrac_to_fractions(f_):
            if not(k and dg):
                continue
            edg = e * dg
            phi = edg // k

            q_solution = self.solve_quadratic(n, phi)
            if q_solution is None:
                continue
            p, q = q_solution
            if p * q == n:
                return p, q
        return None