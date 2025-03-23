from src.application.ElementoDomandaUseCase import GetAllElementiDomandaUseCase
from src.application.ports.ElementiDomandaPorts import GetAllElementiDomandaPort
from src.domain import ElementoDomanda

class GetAllElementiDomandaService(GetAllElementiDomandaUseCase):
    def __init__(self, get_all_port: GetAllElementiDomandaPort):
        self.get_all_port = get_all_port

    def getAllElementiDomanda(self) -> set[ElementoDomanda]:
        return self.get_all_port.getAllElementiDomanda()
