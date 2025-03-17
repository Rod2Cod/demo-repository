from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class UpdateElementiDomandaSetPort(ABC):

    @abstractmethod
    def updateElementiDomandaAssociati(self, nome: str, elementiId: set[int]) -> bool:
        pass