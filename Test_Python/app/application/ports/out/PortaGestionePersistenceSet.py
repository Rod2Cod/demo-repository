from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class PortaGestionePersistenceSet(ABC):

    @abstractmethod
    def saveSet(self, setElementi: SetElementiDomanda) -> bool:
        pass
    
    @abstractmethod
    def getSetByNome(self, nome: str) -> SetElementiDomanda:
        pass

    @abstractmethod
    def deleteSetByNome(self, nome: str) -> SetElementiDomanda:
        pass

    @abstractmethod
    def getAllSet(self) -> set[SetElementiDomanda]:
        pass

    @abstractmethod
    def editNomeSeta(self, nome: str, newNome: str) -> SetElementiDomanda:
        pass

    @abstractmethod
    def updateElementiDomandaAssociati(self, nome: str, elementiId: set[int]) -> bool:
        pass
