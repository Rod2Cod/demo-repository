from src.application.RisultatoTestUseCase import GetAllRisultatiTestUseCase
from src.application.ports.RisultatoTestPorts import GetAllRisultatiTestPort
from src.domain import RisultatoTest

class GetAllRisultatiTestService(GetAllRisultatiTestUseCase):
    def __init__(self, port: GetAllRisultatiTestPort):
        self.port = port

    def getAllRisultatiTest(self) -> set[RisultatoTest]:
        return self.port.getAllRisultatiTest()
