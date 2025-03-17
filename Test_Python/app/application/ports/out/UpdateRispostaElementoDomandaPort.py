from abc import ABC, abstractmethod

class UpdateRispostaElementoDomandaPort(ABC):

    @abstractmethod
    def updateRispostaElementoDomanda(self, idElemento: int, risposta: str) -> bool:
        pass