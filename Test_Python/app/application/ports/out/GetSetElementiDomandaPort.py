from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class GetSetElementiDomandaPort(ABC):

    @abstractmethod
    def getSetElementiDomandaByNome(self, nome: str) -> SetElementiDomanda:
        pass