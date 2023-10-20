from abc import ABC, abstractmethod


class IAttacker(ABC):
    @abstractmethod
    def attack(self, n: int, e: int):
        raise NotImplementedError