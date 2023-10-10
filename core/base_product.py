from abc import ABC, abstractclassmethod
from typing import Union, List, Dict


class BaseProduct(ABC):
    @abstractclassmethod
    def integrate(self, keys: Dict):
        pass

    @abstractclassmethod
    def deintegrate(self):
        pass

    @abstractclassmethod
    def add_ip(self, ip: Union[List[str], str]):
        pass

    @abstractclassmethod
    def remove_ip(self, ip: Union[List[str], str]):
        pass
