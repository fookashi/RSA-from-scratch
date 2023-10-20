from abc import ABC, abstractmethod

class IModInverseCalculator(ABC):
    @abstractmethod
    def calculate_mod_inverse(self, a, m):
        pass