from abc import ABC, abstractmethod
from app.domain import ElementoDomanda

class GetElementoDomandaPort(ABC):

    @abstractmethod
    def getElementoDomanda(self, idElemento: int) -> ElementoDomanda:
        pass