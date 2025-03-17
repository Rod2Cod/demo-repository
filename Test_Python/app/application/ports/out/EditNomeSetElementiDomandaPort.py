from abc import ABC, abstractmethod
from app.domain import SetElementiDomanda

class EditNomeSetElementiDomandaPort(ABC):

    @abstractmethod
    def editNomeSetElementiDomanda(self, nome: str, newNome: str) -> SetElementiDomanda:
        pass