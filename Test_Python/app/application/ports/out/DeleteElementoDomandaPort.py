from abc import ABC, abstractmethod

class DeleteElementoDomandaPort(ABC):

    @abstractmethod
    def deleteElementoDomandaById(self, idElemento: int) -> bool:
        pass