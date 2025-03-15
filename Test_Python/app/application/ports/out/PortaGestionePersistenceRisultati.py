from abc import ABC, abstractmethod
from app.domain import RisultatoTest,RisultatoSingolaDomanda

class PortaGestionePersistenceRisultati(ABC):

    @abstractmethod
    def saveRisultatoTest(self, risultato: RisultatoTest) -> bool:
        pass

    @abstractmethod
    def getRisultatoTestById(self, id: int) -> RisultatoTest:
        pass

    @abstractmethod
    def getAllRisultatoTest(self) -> set[RisultatoTest]:
        pass

    @abstractmethod
    def getAllRisultatoSingolaDomandaByTestId(idTest: int) -> set[RisultatoSingolaDomanda]:
        pass

    @abstractmethod
    def getRisultatoSingolaDomandaTestById(id: int) -> RisultatoSingolaDomanda:
        pass