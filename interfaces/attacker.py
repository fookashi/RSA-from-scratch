from abc import ABC, abstractmethod
from rsa.keys import RSAPublicKey

class IAttacker(ABC):
    @abstractmethod
    def attack(self, public_key: RSAPublicKey):
        raise NotImplementedError