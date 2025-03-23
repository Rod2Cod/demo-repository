from src.application.ElementoDomandaUseCase import GetElementoDomandaUseCase
from src.application.ports.ElementiDomandaPorts import GetElementoDomandaPort
from src.domain import ElementoDomanda

class GetElementoDomandaService(GetElementoDomandaUseCase):
    def __init__(self, get_port: GetElementoDomandaPort):
        self.get_port = get_port

    def getElementoDomandaById(self, id: int) -> ElementoDomanda:
        return self.get_port.getElementoDomandaById(id)
