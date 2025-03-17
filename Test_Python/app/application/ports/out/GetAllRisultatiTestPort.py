from abc import ABC, abstractmethod
from app.domain import RisultatoTest

class GetAllRisultatiTestPort(ABC):

    @abstractmethod
    def getAllRisultatiTest(self) -> set[RisultatoTest]:
        pass