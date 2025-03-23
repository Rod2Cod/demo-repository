from src.domain import ElementoDomanda
from src.application.ports.input import AddElementoDomandaUseCase, GetElementoDomandaUseCase, GetAllElementiDomandaUseCase, DeleteElementiDomandaUseCase, UpdateElementoDomandaUseCase
from src.application.ports.output import SaveElementoDomandaPort, GetElementoDomandaPort, GetAllElementiDomandaPort, DeleteElementiDomandaPort, UpdateElementoDomandaPort

def validateDomandaRisposta(self, domanda: str, risposta: str):
        if not(isinstance(domanda, str) and isinstance(risposta, str)) \
            and (len(domanda) == 0 or len(risposta) == 0):
            raise ValueError("Domanda e risposta devono essere stringhe non vuote.")

def validateId(self, id: int):
    if not isinstance(id, int):
        raise ValueError("Id deve essere un intero.")
    
def validateIdSet(ids: set[int]):
    if(len(ids) == 0):
        raise ValueError("Il set non può essere vuoto.")
    for id in ids:
        if not isinstance(id, int):
            raise ValueError("Il set deve contenere solo valori interi.")

class AddElementoDomandaService(AddElementoDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.__port = port

    def addElementoDomanda(self, domanda: str, risposta: str) -> ElementoDomanda:
        validateDomandaRisposta(domanda, risposta)
        return self.__port.saveElementoDomanda(domanda, risposta)
    
class GetElementoDomandaService(GetElementoDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.__port = port

    def getElementoDomandaById(self, id: int) -> ElementoDomanda:
        validateId(id)
        return self.__port.getElementoDomandaById(id)
    
class GetAllElementiDomandaService(GetAllElementiDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.__port = port

    def getAllElementiDomanda(self) -> set[ElementoDomanda]:
        return self.__port.getAllElementiDomanda()
    
class DeleteElementiDomandaService(DeleteElementiDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.__port = port

    def deleteElementiDomandaById(self, idElementi: set[int]) -> bool:
        validateIdSet(idElementi)
        return self.__port.deleteElementiDomandaById(idElementi)
    
class UpdateElementoDomandaService(UpdateElementoDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.__port = port

    def updateElementoDomandaById(self, id: int, domanda: str, risposta: str) -> bool:
        validateId(id)
        validateDomandaRisposta(domanda, risposta)
        return self.__port.updateElementoDomanda(id, domanda, risposta)