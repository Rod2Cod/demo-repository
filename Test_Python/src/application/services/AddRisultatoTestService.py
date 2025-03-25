from src.application.RisultatoTestUseCase import AddRisultatoTestUseCase
from src.application.ports.RisultatoTestPorts import SaveRisultatoTestPort
from src.domain.dtos import RisultatoTestDTO
from src.domain import RisultatoTest

class AddRisultatoTestService(AddRisultatoTestUseCase):
    def __init__(self, port: SaveRisultatoTestPort):
        self.port = port

    def addRisultatoTest(self, risultatoTestDTO: RisultatoTestDTO) -> bool:
        risultato_test = RisultatoTest.fromDTO(risultatoTestDTO)
        return self.port.saveRisultatoTest(risultato_test)
