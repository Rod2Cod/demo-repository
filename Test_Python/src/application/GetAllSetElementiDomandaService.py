from src.application.SetElementiDomandaUseCase import GetAllSetElementiDomandaUseCase
from src.application.ports.SetElementiDomandaPorts import GetAllSetElementiDomandaPort
from src.domain import SetElementiDomanda

class GetAllSetElementiDomandaService(GetAllSetElementiDomandaUseCase):
    def __init__(self, port: GetAllSetElementiDomandaPort):
        self.port = port

    def getAllSetElementiDomanda(self) -> set[SetElementiDomanda]:
        return self.port.getAllSetElementiDomanda()
