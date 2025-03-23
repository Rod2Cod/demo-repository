from src.application.RisultatoTestUseCase import GetRisultatoSingolaDomandaUseCase
from src.application.ports.RisultatoTestPorts import GetRisultatoSingolaDomandaPort
from src.domain import RisultatoSingolaDomanda

class GetRisultatoSingolaDomandaService(GetRisultatoSingolaDomandaUseCase):
    def __init__(self, port: GetRisultatoSingolaDomandaPort):
        self.port = port

    def getRisultatoSingolaDomandaTestById(self, idTest: int, id: int) -> RisultatoSingolaDomanda:
        return self.port.getRisultatoSingolaDomandaTestById(idTest, id)
