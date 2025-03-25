from src.application.SetElementiDomandaUseCase import AddSetElementiDomandaUseCase
from src.application.ports.SetElementiDomandaPorts import SaveSetElementiDomandaPort
from src.domain import SetElementiDomanda

class AddSetElementiDomandaService(AddSetElementiDomandaUseCase):
    def __init__(self, port: SaveSetElementiDomandaPort):
        self.port = port

    def addSetElementiDomanda(self, nome: str, elementi: set[int]) -> bool:
        set_elementi = SetElementiDomanda(nome=nome, elementi=elementi)
        return self.port.saveSetElementiDomanda(set_elementi)
