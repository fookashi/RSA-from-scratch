import os
import struct

from rsa.utils.transform import bytes2int
from rsa.interfaces import INumberGenerator

class NumberGenerator(INumberGenerator):

    def _read_random_bits(self, nbits: int) -> bytes:
        nbytes, rbits = divmod(nbits, 8)

        # Get the random bytes
        randomdata = os.urandom(nbytes)

        # Add the remaining random bits
        if rbits > 0:
            randomvalue = ord(os.urandom(1))
            randomvalue >>= 8 - rbits
            randomdata = struct.pack("B", randomvalue) + randomdata

        return randomdata

    def generate_number(self, nbits: int) -> int:
        randomdata = self._read_random_bits(nbits)
        value = bytes2int(randomdata)
        # Ensure that the number is large enough to just fill out the required
        # number of bits.
        value |= 1 << (nbits - 1)
        # Ensure that number is odd
        return value | 1

