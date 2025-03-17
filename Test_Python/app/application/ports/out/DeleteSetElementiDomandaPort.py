from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class DeleteSetElementiDomandaPort(ABC):

    @abstractmethod
    def deleteSetElementiDomandaByNome(self, nome: str) -> SetElementiDomanda:
        pass