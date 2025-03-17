from abc import ABC, abstractmethod
from app.domain import RisultatoSingolaDomanda

class GetRisultatoSingolaDomandaPort(ABC):

    @abstractmethod
    def getRisultatoSingolaDomandaTestById(id: int) -> RisultatoSingolaDomanda:
        pass