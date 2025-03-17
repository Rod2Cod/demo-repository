from abc import ABC, abstractmethod
from app.domain import RisultatoSingolaDomanda

class GetAllRisultatiSingoleDomandeTestPort(ABC):
    
    @abstractmethod
    def getAllRisultatiSingoleDomandeByTestId(self, id: int) -> set[RisultatoSingolaDomanda]:
        pass