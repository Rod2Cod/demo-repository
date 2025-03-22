from src.domain import ElementoDomanda
from src.application.ports.input import AddElementoDomandaUseCase, GetElementoDomandaUseCase
from src.application.ports.output import SaveElementoDomandaPort

class AddElementoDomandaService(AddElementoDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.savePort = port

    def addElementoDomanda(self, domanda: str, risposta: str) -> ElementoDomanda:
        #return self.port.saveElementoDomanda(domanda, risposta)
        return {"domanda": domanda, "risposta": risposta}
    
class GetElementoDomandaService(GetElementoDomandaUseCase):
    def __init__(self, port: SaveElementoDomandaPort):
        self.getPort = port

    def getElementoDomandaById(self, id: int) -> ElementoDomanda:
        #return self.port.saveElementoDomanda(domanda, risposta)
        return {"id": id}
    
class GetAllElementiDomandaService:
    def __init__(self, port: SaveElementoDomandaPort):
        self.getPort = port

    def getAllElementiDomanda(self) -> set[ElementoDomanda]:
        #return self.port.saveElementoDomanda(domanda, risposta)
        return [{"id": 1}, {"id": 2}]
    
class DeleteElementiDomandaService:
    def __init__(self, port: SaveElementoDomandaPort):
        self.getPort = port

    def deleteElementiDomanda(self, id: int) -> bool:
        #return self.port.saveElementoDomanda(domanda, risposta)
        return True
    
class UpdateElementoDomandaService:
    def __init__(self, port: SaveElementoDomandaPort):
        self.getPort = port

    def updateElementoDomanda(self, id: int, domanda: str, risposta: str) -> bool:
        #return self.port.saveElementoDomanda(domanda, risposta)
        return {"id": id, "domanda": domanda, "risposta": risposta}