from src.application.RisultatoTestUseCase import GetRisultatoTestUseCase
from src.application.ports.RisultatoTestPorts import GetRisultatoTestPort
from src.domain import RisultatoTest

class GetRisultatoTestService(GetRisultatoTestUseCase):
    def __init__(self, port: GetRisultatoTestPort):
        self.port = port

    def getRisultatoTestById(self, id: int) -> RisultatoTest:
        return self.port.getRisultatoTestById(id)
