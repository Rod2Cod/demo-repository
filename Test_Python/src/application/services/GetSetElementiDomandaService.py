from src.application.SetElementiDomandaUseCase import GetSetElementiDomandaUseCase
from src.application.ports.SetElementiDomandaPorts import GetSetElementiDomandaPort
from src.domain import SetElementiDomanda

class GetSetElementiDomandaService(GetSetElementiDomandaUseCase):
    def __init__(self, port: GetSetElementiDomandaPort):
        self.port = port

    def getSetElementiDomandaByNome(self, nome: str) -> SetElementiDomanda:
        return self.port.getSetElementiDomandaByNome(nome)
