from abc import ABC, abstractmethod
from app.domain import ElementoDomanda

class SaveElementoDomandaPort(ABC):

    @abstractmethod
    def saveElementoDomanda(self, elemento: ElementoDomanda) -> bool:
        pass
    
class GetElementoDomandaPort(ABC):

    @abstractmethod
    def getElementoDomanda(self, idElemento: int) -> ElementoDomanda:
        pass
    
class GetAllElementiDomandaPort(ABC):

    @abstractmethod
    def getAllElementoDomanda(self) -> set[ElementoDomanda]:
        pass
    
class DeleteElementoDomandaPort(ABC):

    @abstractmethod
    def deleteElementoDomandaById(self, idElemento: int) -> bool:
        pass
    
class UpdateDomandaElementoDomandaPort(ABC):

    @abstractmethod
    def updateDomandaElementoDomanda(self, idElemento: int, domanda: str) -> bool:
        pass
    
class UpdateRispostaElementoDomandaPort(ABC):

    @abstractmethod
    def updateRispostaElementoDomanda(self, idElemento: int, risposta: str) -> bool:
        pass