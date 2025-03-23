from src.application.RisultatoTestUseCase import GetAllRisultatiSingoleDomandeUseCase
from src.application.ports.RisultatoTestPorts import GetAllRisultatiSingoleDomandeTestPort
from src.domain import RisultatoSingolaDomanda

class GetAllRisultatiSingoleDomandeService(GetAllRisultatiSingoleDomandeUseCase):
    def __init__(self, port: GetAllRisultatiSingoleDomandeTestPort):
        self.port = port

    def getAllRisultatiSingoleDomandeByTestId(self, idTest: int) -> set[RisultatoSingolaDomanda]:
        return self.port.getAllRisultatiSingoleDomandeByTestId(idTest)
