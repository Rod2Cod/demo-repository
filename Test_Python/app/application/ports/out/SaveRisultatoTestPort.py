from abc import ABC, abstractmethod
from app.domain import RisultatoTest

class SaveRisultatoTestPort(ABC):

    @abstractmethod
    def saveRisultatoTest(self, risultato: RisultatoTest) -> bool:
        pass