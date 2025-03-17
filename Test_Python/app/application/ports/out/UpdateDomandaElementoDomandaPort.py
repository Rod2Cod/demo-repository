from abc import ABC, abstractmethod

class UpdateDomandaElementoDomandaPort(ABC):

    @abstractmethod
    def updateDomandaElementoDomanda(self, idElemento: int, domanda: str) -> bool:
        pass