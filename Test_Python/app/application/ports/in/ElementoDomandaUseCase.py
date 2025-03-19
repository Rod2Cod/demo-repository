from abc import ABC, abstractmethod
from app.domain import ElementoDomanda

class AddElementoDomandaUseCase(ABC):
    @abstractmethod
    def addElementoDomanda(self, domanda: str, risposta: str) -> ElementoDomanda:
        pass
    
class GetElementoDomandaUseCase(ABC):
    @abstractmethod
    def getElementoDomandaById(self, id: int) -> ElementoDomanda:
        pass
    
class GetAllElementiDomandaUseCase(ABC):
    @abstractmethod
    def getAllElementiDomanda(self) -> set[ElementoDomanda]:
        pass
    
class DeleteElementiDomandaUseCase(ABC):
    @abstractmethod
    def deleteElementiDomandaById(self, Ids: set[int]) -> bool:
        pass
    
class UpdateDomandaElementoDomandaUseCase(ABC):
    @abstractmethod
    def updateDomandaElementoDomanda(self, id: int, domanda: str) -> bool:
        pass
    
class UpdateRispostaElementoDomandaUseCase(ABC):
    @abstractmethod
    def updateRispostaElementoDomanda(self, id: int, risposta: str) -> bool:
        pass