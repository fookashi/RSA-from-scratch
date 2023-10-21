from rsa.utils.newton_sq_root import isqrt
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

    def _contfrac_to_rational_iter(self, contfrac: Iterable[int]) -> Iterator[tuple[int, int]]:
        n0, d0 = 0, 1
        n1, d1 = 1, 0
        for q in contfrac:
            n = q * n1 + n0
            d = q * d1 + d0
            yield n, d
            n0, d0 = n1, d1
            n1, d1 = n, d

    def _convergents_from_contfrac(self, contfrac: Iterable[int]) -> Iterator[tuple[int, int]]:
        n_, d_ = 1, 0
        for i, (n, d) in enumerate(self._contfrac_to_rational_iter(contfrac)):
            if i % 2 == 0:
                yield n + n_, d + d_
            else:
                yield n, d
            n_, d_ = n, d
            
    def attack(self, public_key: RSAPublicKey):
        e, n = public_key.e, public_key.n
        f_ = self._rational_to_contfrac(e, n)
        for k, dg in self._convergents_from_contfrac(f_):
            edg = e * dg
            phi = edg // k

            x = n - phi + 1
            if x % 2 == 0 and self._is_perfect_square((x // 2) ** 2 - n):
                g = edg - phi * k
                return dg // g
        return None