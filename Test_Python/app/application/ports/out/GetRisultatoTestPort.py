from abc import ABC, abstractmethod
from app.domain import RisultatoTest

class GetRisultatoTestPort(ABC):

    @abstractmethod
    def getRisultatoTestById(self, id: int) -> RisultatoTest:
        pass