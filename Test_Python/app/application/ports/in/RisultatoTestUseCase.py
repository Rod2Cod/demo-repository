from abc import ABC, abstractmethod
from app.domain import RisultatoTest, RisultatoSingolaDomanda

class AddRisultatoTestUseCase(ABC):
    @abstractmethod
    def addRisultatoTest(self) -> bool:
        pass
    
class GetRisultatoTestUseCase(ABC):
    @abstractmethod
    def getRisultatoTestById(self, id: int) -> RisultatoTest:
        pass
    
class GetAllRisultatiTestUseCase(ABC):
    @abstractmethod
    def getAllRisultatiTest(self) -> set[RisultatoTest]:
        pass
    
class GetAllRisultatiSingoleDomandeUseCase(ABC):
    @abstractmethod
    def getAllRisultatiSingoleDomandeByTestId(self, idTest: int) -> set[RisultatoSingolaDomanda]:
        pass
    
class GetRisultatoSingolaDomandaUseCase(ABC):
    @abstractmethod
    def getRisultatoSingolaDomandaTestById(self, idTest: int, id: int) -> RisultatoSingolaDomanda:
        pass