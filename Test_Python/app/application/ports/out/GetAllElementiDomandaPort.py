from abc import ABC, abstractmethod
from app.domain import ElementoDomanda

class GetAllElementiDomandaPort(ABC):

    @abstractmethod
    def getAllElementoDomanda(self) -> set[ElementoDomanda]:
        pass