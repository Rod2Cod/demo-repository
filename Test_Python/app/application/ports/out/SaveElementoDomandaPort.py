from abc import ABC, abstractmethod
from app.domain import ElementoDomanda

class SaveElementoDomandaPort(ABC):

    @abstractmethod
    def saveElementoDomanda(self, elemento: ElementoDomanda) -> bool:
        pass