from src.application.ElementoDomandaUseCase import AddElementoDomandaUseCase
from src.application.ports.ElementiDomandaPorts import SaveElementoDomandaPort
from src.domain import ElementoDomanda

class AddElementoDomandaService(AddElementoDomandaUseCase):
    def __init__(self, save_port: SaveElementoDomandaPort):
        self.save_port = save_port

    def addElementoDomanda(self, domanda: str, risposta: str) -> ElementoDomanda:
        elemento = ElementoDomanda(domanda=domanda, risposta=risposta)
        return self.save_port.saveElementoDomanda(elemento)
