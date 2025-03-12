from abc import ABC, abstractmethod
from app.Domain import SetElementiDomanda

class PortaGestionePersistenceSet(ABC):

    @abstractmethod
    def saveSetElementiDomanda(self, setElementi: SetElementiDomanda) -> bool:
        pass
    
    @abstractmethod
    def getSetElementiDomandaByName(self, name: str) -> SetElementiDomanda:
        pass

    @abstractmethod
    def deleteSetElementiDomandaByName(self, name: str) -> SetElementiDomanda:
        pass

    @abstractmethod
    def getAllSetElementiDomanda(self) -> set[SetElementiDomanda]:
        pass

    @abstractmethod
    def editNomeSetElementiDomanda(self, name: str, newName: str) -> SetElementiDomanda:
        pass
