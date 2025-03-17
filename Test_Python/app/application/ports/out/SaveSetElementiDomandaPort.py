from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class SaveSetElementiDomandaPort(ABC):

    @abstractmethod
    def SaveSetElementiDomandaPort(self, setElementi: SetElementiDomanda) -> bool:
        pass