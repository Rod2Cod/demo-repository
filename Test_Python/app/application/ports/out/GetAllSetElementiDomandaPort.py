from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class GetAllSetElementiDomandaPort(ABC):

    @abstractmethod
    def getAllSetElementiDomanda(self) -> set[SetElementiDomanda]:
        pass