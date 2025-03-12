from abc import ABC, abstractmethod
from app.Domain import ElementoDomanda

class PortaGestionePersistenceDomande(ABC):

    @abstractmethod
    def saveElementoDomanda(self, elemento: ElementoDomanda):
        pass
    
    @abstractmethod
    def getElementoDomanda(self, idElemento: int) -> ElementoDomanda:
        pass

    @abstractmethod
    def deleteElementoDomandaById(self, idElemento: int) -> ElementoDomanda:
        pass

    @abstractmethod
    def getAllElementoDomanda(self) -> set[ElementoDomanda]:
        pass

    @abstractmethod
    def updateDomandaElementoDomanda(self, idElemento: int, domanda: str) -> bool:
        pass

    @abstractmethod
    def updateRispostaElementoDomanda(self, idElemento: int, risposta: str) -> bool:
        pass