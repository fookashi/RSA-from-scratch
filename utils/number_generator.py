import os
import struct

from .transform import bytes2int

class NumberGenerator:

    def _read_random_bits(self, nbits) -> bytes:
        nbytes, rbits = divmod(nbits, 8)

        # Get the random bytes
        randomdata = os.urandom(nbytes)

        # Add the remaining random bits
        if rbits > 0:
            randomvalue = ord(os.urandom(1))
            randomvalue >>= 8 - rbits
            randomdata = struct.pack("B", randomvalue) + randomdata

        return randomdata

    def read_random_int(self, nbits: int):
        randomdata = self._read_random_bits(nbits)
        value = bytes2int(randomdata)
        # Ensure that the number is large enough to just fill out the required
        # number of bits.
        value |= 1 << (nbits - 1)
        return value

    def read_random_odd_int(self, nbits: int):
        value = self.read_random_int(nbits)

        return value | 1

